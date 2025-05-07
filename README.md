# 🤖 Jarvis Assistant (Python + OpenRouter)

A smart and modular AI assistant built in Python using the OpenRouter API (ChatGPT-style).  
This is the beginning of a fully upgradeable JARVIS system.

---

## 🚀 Features (v0.1)
- Text-based interaction via terminal
- OpenRouter integration using `mistral-7b-instruct`
- `.env` based API key security
- Cross-platform & virtualenv compatible

---

## 📦 Setup

1. **Clone the repo**

git clone https://github.com/MaazHussain2711/jarvis-assistant.git
`cd jarvis-assistant`

2. **Create & activate virtual environment**
`python -m venv venv`

# Windows
`venv\Scripts\activate`

# Linux/macOS
`source venv/bin/activate`

3. Install requirements
`pip install -r requirements.txt`

Create a .env file
`OPENROUTER_API_KEY=your_openrouter_key_here`

Run the assistant
`python jarvis.py`


🛠️ Tech Stack
Python 3.11

OpenRouter API

dotenv

requests

📚 Roadmap
 Voice input/output (TTS & STT)

 GUI (PyQt5 or Tkinter)

 Local/offline LLM support

 Plugin system for modular tools

 Web actions (YouTube search, open browser, etc.)

 JARVIS Modes (formal, casual, sarcastic...)

💡 Credits
Created with ❤️ by Maaz Hussain

📄 License
This project is open-source under the MIT License.

### ✅ Bonus: Create `requirements.txt`

In terminal: pip freeze > requirements.txt
