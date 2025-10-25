#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit
import subprocess
import os
import sys
import threading
import pty
import select
import termios
import struct
import fcntl
import uuid
from typing import Any, Dict
from hackingtool import all_tools

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackingtool-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store active terminal sessions and approved commands
active_sessions = {}
approved_commands = {}

def get_all_tools_data():
    """Extract all tools and categories from hackingtool"""
    categories = []
    
    for tool_collection in all_tools:
        category = {
            'title': tool_collection.TITLE,
            'description': getattr(tool_collection, 'DESCRIPTION', ''),
            'tools': []
        }
        
        if hasattr(tool_collection, 'TOOLS'):
            for tool in tool_collection.TOOLS:
                tool_data = {
                    'title': tool.TITLE,
                    'description': getattr(tool, 'DESCRIPTION', 'No description available'),
                    'project_url': getattr(tool, 'PROJECT_URL', ''),
                    'has_install': bool(getattr(tool, 'INSTALL_COMMANDS', [])),
                    'has_run': bool(getattr(tool, 'RUN_COMMANDS', [])) or hasattr(tool, 'run'),
                    'install_commands': getattr(tool, 'INSTALL_COMMANDS', []),
                    'run_commands': getattr(tool, 'RUN_COMMANDS', [])
                }
                category['tools'].append(tool_data)
        
        categories.append(category)
    
    return categories

@app.route('/')
def index():
    categories = get_all_tools_data()
    return render_template('index.html', categories=categories)

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/api/tool/info', methods=['POST'])
def tool_info():
    data: Dict[str, Any] = request.json or {}
    category_idx = data.get('category_idx')
    tool_idx = data.get('tool_idx')
    
    try:
        if category_idx is None or tool_idx is None:
            return jsonify({'success': False, 'error': 'Missing category or tool index'})
        
        tool_collection = all_tools[category_idx]
        tool = tool_collection.TOOLS[tool_idx]
        
        return jsonify({
            'success': True,
            'title': tool.TITLE,
            'description': getattr(tool, 'DESCRIPTION', 'No description'),
            'project_url': getattr(tool, 'PROJECT_URL', ''),
            'install_commands': getattr(tool, 'INSTALL_COMMANDS', []),
            'run_commands': getattr(tool, 'RUN_COMMANDS', [])
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/tool/install', methods=['POST'])
def install_tool():
    data: Dict[str, Any] = request.json or {}
    category_idx = data.get('category_idx')
    tool_idx = data.get('tool_idx')
    
    try:
        if category_idx is None or tool_idx is None:
            return jsonify({'success': False, 'error': 'Missing category or tool index'})
        
        tool_collection = all_tools[category_idx]
        tool = tool_collection.TOOLS[tool_idx]
        
        # Get install commands
        install_commands = getattr(tool, 'INSTALL_COMMANDS', [])
        
        if not install_commands:
            return jsonify({'success': False, 'message': 'No installation commands available'})
        
        # Execute installation
        output = []
        for cmd in install_commands:
            output.append(f"$ {cmd}")
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
                output.append(result.stdout if result.stdout else result.stderr)
            except subprocess.TimeoutExpired:
                output.append("Command timed out after 30 seconds")
            except Exception as e:
                output.append(f"Error: {str(e)}")
        
        return jsonify({
            'success': True,
            'message': f'{tool.TITLE} installation attempted',
            'output': '\n'.join(output)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/tool/run-interactive', methods=['POST'])
def run_tool_interactive():
    """Start an interactive terminal session for a tool"""
    data: Dict[str, Any] = request.json or {}
    category_idx = data.get('category_idx')
    tool_idx = data.get('tool_idx')
    
    try:
        if category_idx is None or tool_idx is None:
            return jsonify({'success': False, 'error': 'Missing category or tool index'})
        
        tool_collection = all_tools[category_idx]
        tool = tool_collection.TOOLS[tool_idx]
        
        # Determine the command to run
        command = None
        run_commands = getattr(tool, 'RUN_COMMANDS', [])
        
        if run_commands:
            # Use the first run command
            command = run_commands[0]
        elif hasattr(tool, 'run'):
            # For tools with run() method, we'll try to execute them in terminal mode
            return jsonify({
                'success': False,
                'message': 'This tool uses a custom run method. It may not support interactive mode.',
                'fallback': True
            })
        else:
            return jsonify({
                'success': False,
                'message': 'No run commands available for this tool.'
            })
        
        # Generate a unique session ID for this command
        session_id = str(uuid.uuid4())
        
        # Store the approved command server-side (SECURITY: Never trust client)
        approved_commands[session_id] = {
            'command': command,
            'tool_name': tool.TITLE
        }
        
        # Return session info - actual execution happens via WebSocket with session_id
        return jsonify({
            'success': True,
            'title': tool.TITLE,
            'session_id': session_id,
            'message': f'Interactive session ready for {tool.TITLE}'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def set_winsize(fd, rows, cols):
    """Set terminal window size"""
    winsize = struct.pack("HHHH", rows, cols, 0, 0)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

def read_and_forward_pty_output(fd, sid):
    """Read from PTY and forward to WebSocket"""
    max_read_bytes = 1024 * 20
    while True:
        try:
            socketio.sleep(0.01)  # type: ignore
            if sid not in active_sessions:
                break
            timeout_sec = 0
            (data_ready, _, _) = select.select([fd], [], [], timeout_sec)
            if data_ready:
                output = os.read(fd, max_read_bytes).decode('utf-8', errors='replace')
                socketio.emit('terminal_output', {'output': output}, to=sid)  # type: ignore
        except OSError:
            break

@socketio.on('start_terminal')
def handle_start_terminal(data):
    """Start a new terminal session with pre-approved command"""
    session_id = data.get('session_id')
    sid = request.sid  # type: ignore
    
    # SECURITY: Only execute pre-approved commands
    if not session_id or session_id not in approved_commands:
        emit('terminal_error', {'error': 'Invalid or expired session. Please start the tool again.'})
        return
    
    try:
        # Get the approved command
        command_data = approved_commands[session_id]
        command = command_data['command']
        
        # Remove from approved list (one-time use)
        del approved_commands[session_id]
        
        # Get current working directory (project root)
        project_root = os.getcwd()
        
        # Create PTY
        (child_pid, fd) = pty.fork()
        
        if child_pid == 0:
            # Child process - stay in project root where tools are
            os.chdir(project_root)
            # Execute the command with proper shell handling
            os.execvp('/bin/bash', ['/bin/bash', '-c', command])
        else:
            # Parent process
            active_sessions[sid] = {
                'pid': child_pid,
                'fd': fd
            }
            
            # Set terminal size
            set_winsize(fd, 24, 80)
            
            # Start thread to read PTY output
            socketio.start_background_task(target=read_and_forward_pty_output, fd=fd, sid=sid)
            
            emit('terminal_ready', {'status': 'connected'})
            
    except Exception as e:
        print(f"Terminal error: {str(e)}")
        emit('terminal_error', {'error': str(e)})

@socketio.on('terminal_input')
def handle_terminal_input(data):
    """Handle input from client terminal"""
    sid = request.sid  # type: ignore
    if sid in active_sessions:
        fd = active_sessions[sid]['fd']
        try:
            os.write(fd, data['input'].encode())
        except OSError:
            pass

@socketio.on('terminal_resize')
def handle_terminal_resize(data):
    """Handle terminal resize"""
    sid = request.sid  # type: ignore
    if sid in active_sessions:
        fd = active_sessions[sid]['fd']
        set_winsize(fd, data['rows'], data['cols'])

@socketio.on('disconnect')
def handle_disconnect():
    """Clean up terminal session on disconnect"""
    sid = request.sid  # type: ignore
    if sid in active_sessions:
        try:
            os.close(active_sessions[sid]['fd'])
            os.kill(active_sessions[sid]['pid'], 9)
        except:
            pass
        del active_sessions[sid]

if __name__ == '__main__':
    # Ensure running on all interfaces for Replit
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True, use_reloader=True, log_output=True)  # type: ignore
