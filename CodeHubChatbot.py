import React, { useState } from 'react';
import { Copy, Check, Folder, File } from 'lucide-react';

const CodeBlock = ({ title, code, language = "bash" }) => {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="mb-6">
      <div className="flex items-center justify-between bg-gray-800 px-4 py-2 rounded-t-lg">
        <span className="text-gray-300 font-semibold">{title}</span>
        <button
          onClick={copyToClipboard}
          className="flex items-center gap-2 bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded transition-colors"
        >
          {copied ? (
            <>
              <Check size={16} className="text-green-400" />
              <span className="text-green-400 text-sm">Copied!</span>
            </>
          ) : (
            <>
              <Copy size={16} className="text-gray-300" />
              <span className="text-gray-300 text-sm">Copy</span>
            </>
          )}
        </button>
      </div>
      <pre className="bg-gray-900 p-4 rounded-b-lg overflow-x-auto">
        <code className="text-gray-100 text-sm font-mono">{code}</code>
      </pre>
    </div>
  );
};

const FileTree = () => {
  return (
    <div className="bg-gray-800 p-4 rounded-lg mb-6">
      <h3 className="text-white font-semibold mb-3 flex items-center gap-2">
        <Folder className="text-yellow-400" size={20} />
        Project Structure
      </h3>
      <div className="font-mono text-sm text-gray-300 space-y-1">
        <div>chatbot-web/</div>
        <div className="pl-4">├── <File className="inline text-blue-400" size={14} /> index.html</div>
        <div className="pl-4">├── <File className="inline text-blue-400" size={14} /> style.css</div>
        <div className="pl-4">├── <File className="inline text-blue-400" size={14} /> script.js</div>
        <div className="pl-4">├── <File className="inline text-blue-400" size={14} /> README.md</div>
        <div className="pl-4">└── <File className="inline text-blue-400" size={14} /> .gitignore</div>
      </div>
    </div>
  );
};

export default function GitHubChatbotGuide() {
  const htmlCode = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chatbot</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>AI Chatbot</h1>
        </div>
        <div class="chat-messages" id="chatMessages">
            <div class="message bot-message">
                <p>Hello! I'm your AI assistant. How can I help you today?</p>
            </div>
        </div>
        <div class="chat-input-container">
            <input 
                type="text" 
                id="userInput" 
                placeholder="Type your message..." 
                class="chat-input"
            >
            <button onclick="sendMessage()" class="send-button">Send</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>`;

  const cssCode = `* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chat-container {
    width: 90%;
    max-width: 600px;
    height: 80vh;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.chat-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    text-align: center;
}

.chat-messages {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.message {
    max-width: 70%;
    padding: 12px 16px;
    border-radius: 18px;
    animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.user-message {
    background: #667eea;
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}

.bot-message {
    background: #f0f0f0;
    color: #333;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}

.chat-input-container {
    display: flex;
    padding: 20px;
    background: #f9f9f9;
    border-top: 1px solid #e0e0e0;
}

.chat-input {
    flex: 1;
    padding: 12px 16px;
    border: 2px solid #e0e0e0;
    border-radius: 25px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.3s;
}

.chat-input:focus {
    border-color: #667eea;
}

.send-button {
    margin-left: 10px;
    padding: 12px 24px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    font-weight: bold;
    transition: transform 0.2s;
}

.send-button:hover {
    transform: scale(1.05);
}

.send-button:active {
    transform: scale(0.95);
}`;

  const jsCode = `function sendMessage() {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    
    if (message === '') return;
    
    // Add user message
    addMessage(message, 'user-message');
    input.value = '';
    
    // Simulate bot response
    setTimeout(() => {
        const botResponse = getBotResponse(message);
        addMessage(botResponse, 'bot-message');
    }, 500);
}

function addMessage(text, className) {
    const messagesContainer = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = \`message \${className}\`;
    messageDiv.innerHTML = \`<p>\${text}</p>\`;
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function getBotResponse(userMessage) {
    const responses = {
        'hello': 'Hello! How can I assist you today?',
        'hi': 'Hi there! What can I do for you?',
        'how are you': "I'm doing great! Thanks for asking. How can I help you?",
        'bye': 'Goodbye! Have a great day!',
        'help': 'I can answer questions and have a conversation with you. Try asking me something!',
    };
    
    const lowerMessage = userMessage.toLowerCase();
    
    for (let key in responses) {
        if (lowerMessage.includes(key)) {
            return responses[key];
        }
    }
    
    return "I understand. Could you tell me more about that?";
}

// Allow Enter key to send message
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});`;

  const readmeCode = `# AI Chatbot Web Application

A simple, elegant chatbot web interface built with vanilla HTML, CSS, and JavaScript.

## Features

- Clean and modern UI design
- Responsive layout
- Smooth animations
- Easy to customize

## Setup

1. Clone this repository
2. Open \`index.html\` in your web browser
3. Start chatting!

## Customization

- Edit \`script.js\` to add more bot responses
- Modify \`style.css\` to change the appearance
- Update \`index.html\` for structure changes

## Future Enhancements

- Connect to AI API (OpenAI, Claude, etc.)
- Add chat history persistence
- Include typing indicators
- Add file upload capability

## License

MIT License - Feel free to use and modify!`;

  const gitignoreCode = `# Dependencies
node_modules/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log`;

  const setupCommands = `# Create project directory
mkdir chatbot-web
cd chatbot-web

# Initialize git repository
git init

# Create files
touch index.html style.css script.js README.md .gitignore

# Add all files
git add .

# First commit
git commit -m "Initial commit: Basic chatbot structure"

# Connect to GitHub (replace USERNAME and REPO)
git remote add origin https://github.com/USERNAME/REPO.git

# Push to GitHub
git branch -M main
git push -u origin main`;

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 p-6">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">GitHub Chatbot Project</h1>
          <p className="text-gray-400">Complete code structure and setup guide</p>
        </div>

        <FileTree />

        <CodeBlock title="index.html" code={htmlCode} language="html" />
        
        <CodeBlock title="style.css" code={cssCode} language="css" />
        
        <CodeBlock title="script.js" code={jsCode} language="javascript" />
        
        <CodeBlock title="README.md" code={readmeCode} language="markdown" />
        
        <CodeBlock title=".gitignore" code={gitignoreCode} language="text" />
        
        <CodeBlock title="Git Setup Commands" code={setupCommands} language="bash" />

        <div className="bg-blue-900 border border-blue-700 rounded-lg p-4 mt-6">
          <h3 className="text-blue-200 font-semibold mb-2">📝 Quick Start</h3>
          <ol className="text-blue-100 text-sm space-y-2">
            <li>1. Create a new repository on GitHub</li>
            <li>2. Run the Git Setup Commands above</li>
            <li>3. Replace USERNAME and REPO with your details</li>
            <li>4. Open index.html in a browser to test</li>
          </ol>
        </div>
      </div>
    </div>
  );
}
