// Global variables
let socket = null;
let term = null;
let fitAddon = null;

// Toggle category visibility
function toggleCategory(index) {
    const content = document.getElementById(`category-${index}`);
    const icon = content.previousElementSibling.querySelector('.toggle-icon');
    
    if (content.classList.contains('active')) {
        content.classList.remove('active');
        icon.style.transform = 'rotate(0deg)';
    } else {
        content.classList.add('active');
        icon.style.transform = 'rotate(180deg)';
    }
}

// Search functionality
function searchTools() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const toolCards = document.querySelectorAll('.tool-card');
    
    toolCards.forEach(card => {
        const toolName = card.getAttribute('data-tool-name');
        const toolDesc = card.querySelector('.tool-desc').textContent.toLowerCase();
        
        if (toolName.includes(searchInput) || toolDesc.includes(searchInput)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Show loading spinner
function showSpinner() {
    document.getElementById('loadingSpinner').style.display = 'flex';
}

// Hide loading spinner
function hideSpinner() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

// Show modal
function showModal(title, message, output, isSuccess = true) {
    const modal = document.getElementById('outputModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalStatus = document.getElementById('modalStatus');
    const modalOutput = document.getElementById('modalOutput');
    
    modalTitle.textContent = title;
    modalStatus.textContent = message;
    modalStatus.className = isSuccess ? 'status-message status-success' : 'status-message status-error';
    modalOutput.textContent = output || 'No output available';
    
    modal.style.display = 'block';
}

// Close modal
function closeModal() {
    document.getElementById('outputModal').style.display = 'none';
}

// Initialize terminal
function initializeTerminal() {
    if (!term) {
        term = new Terminal({
            cursorBlink: true,
            fontSize: 14,
            fontFamily: 'Courier New, monospace',
            theme: {
                background: '#1e1e1e',
                foreground: '#d4d4d4',
                cursor: '#ffffff',
                selection: '#264f78',
                black: '#000000',
                red: '#cd3131',
                green: '#0dbc79',
                yellow: '#e5e510',
                blue: '#2472c8',
                magenta: '#bc3fbc',
                cyan: '#11a8cd',
                white: '#e5e5e5',
                brightBlack: '#666666',
                brightRed: '#f14c4c',
                brightGreen: '#23d18b',
                brightYellow: '#f5f543',
                brightBlue: '#3b8eea',
                brightMagenta: '#d670d6',
                brightCyan: '#29b8db',
                brightWhite: '#e5e5e5'
            }
        });
        
        fitAddon = new FitAddon.FitAddon();
        term.loadAddon(fitAddon);
    }
}

// Open terminal modal
function openTerminal(title, sessionId) {
    const modal = document.getElementById('terminalModal');
    const terminalTitle = document.getElementById('terminalTitle');
    const terminalContainer = document.getElementById('terminal');
    
    terminalTitle.textContent = `Interactive Terminal - ${title}`;
    
    // Clear terminal container
    terminalContainer.innerHTML = '';
    
    // Initialize terminal
    initializeTerminal();
    term.open(terminalContainer);
    
    // Fit terminal to container
    setTimeout(() => {
        fitAddon.fit();
    }, 100);
    
    // Show modal
    modal.style.display = 'block';
    
    // Initialize WebSocket connection
    if (!socket || !socket.connected) {
        socket = io();
        
        socket.on('connect', () => {
            console.log('WebSocket connected');
            // Start terminal session with the session_id (secure)
            socket.emit('start_terminal', { session_id: sessionId });
        });
        
        socket.on('terminal_ready', (data) => {
            console.log('Terminal ready:', data);
        });
        
        socket.on('terminal_output', (data) => {
            term.write(data.output);
        });
        
        socket.on('terminal_error', (data) => {
            term.write(`\r\n\x1b[31mError: ${data.error}\x1b[0m\r\n`);
        });
        
        socket.on('disconnect', () => {
            console.log('WebSocket disconnected');
            term.write('\r\n\x1b[33mConnection closed\x1b[0m\r\n');
        });
    } else {
        // Reuse existing connection
        socket.emit('start_terminal', { session_id: sessionId });
    }
    
    // Handle terminal input
    term.onData((data) => {
        if (socket && socket.connected) {
            socket.emit('terminal_input', { input: data });
        }
    });
    
    // Handle window resize
    window.addEventListener('resize', () => {
        if (fitAddon && modal.style.display === 'block') {
            fitAddon.fit();
            const dimensions = fitAddon.proposeDimensions();
            if (socket && socket.connected && dimensions) {
                socket.emit('terminal_resize', {
                    rows: dimensions.rows,
                    cols: dimensions.cols
                });
            }
        }
    });
}

// Close terminal
function closeTerminal() {
    const modal = document.getElementById('terminalModal');
    modal.style.display = 'none';
    
    // Disconnect socket
    if (socket && socket.connected) {
        socket.disconnect();
        socket = null;
    }
    
    // Dispose terminal
    if (term) {
        term.dispose();
        term = null;
        fitAddon = null;
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const outputModal = document.getElementById('outputModal');
    const terminalModal = document.getElementById('terminalModal');
    
    if (event.target == outputModal) {
        closeModal();
    }
    
    if (event.target == terminalModal) {
        closeTerminal();
    }
}

// Install tool
async function installTool(categoryIdx, toolIdx, toolName) {
    showSpinner();
    
    try {
        const response = await fetch('/api/tool/install', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                category_idx: categoryIdx,
                tool_idx: toolIdx
            })
        });
        
        const data = await response.json();
        hideSpinner();
        
        if (data.success) {
            showModal(
                `Installing: ${toolName}`,
                data.message,
                data.output,
                true
            );
        } else {
            showModal(
                `Installation Failed: ${toolName}`,
                data.error || data.message,
                data.output || 'Installation failed',
                false
            );
        }
    } catch (error) {
        hideSpinner();
        showModal(
            'Error',
            'Failed to install tool',
            error.toString(),
            false
        );
    }
}

// Run tool interactively
async function runToolInteractive(categoryIdx, toolIdx, toolName) {
    showSpinner();
    
    try {
        const response = await fetch('/api/tool/run-interactive', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                category_idx: categoryIdx,
                tool_idx: toolIdx
            })
        });
        
        const data = await response.json();
        hideSpinner();
        
        if (data.success) {
            // Open interactive terminal with session_id
            openTerminal(toolName, data.session_id);
        } else if (data.fallback) {
            // Tool doesn't support interactive mode, show info
            showModal(
                `Info: ${toolName}`,
                data.message,
                'This tool may need to be run from the Console tab for full functionality.',
                false
            );
        } else {
            showModal(
                `Run Failed: ${toolName}`,
                data.error || data.message,
                'Unable to run this tool',
                false
            );
        }
    } catch (error) {
        hideSpinner();
        showModal(
            'Error',
            'Failed to run tool',
            error.toString(),
            false
        );
    }
}

// Open first category by default
document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.category-card')) {
        toggleCategory(0);
    }
});
