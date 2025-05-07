# VERSION1.1.py (v1.1 - Voice Output)

import os
import requests
import pyttsx3
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Setup text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """
    Speaks the given text using pyttsx3.
    """
    engine.say(text)
    engine.runAndWait()


def ask_jarvis(prompt):
    """
    Sends a prompt to OpenRouter API and returns the response.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourapp.com",  # Put your domain/project name
        "X-Title": "jarvis-assistant"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful and intelligent assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        return reply
    else:
        return f"Error: {response.status_code} - {response.text}"


# Main loop
if __name__ == "__main__":
    print("🎙️ Jarvis with Voice is online. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            speak("Goodbye!")
            print("Jarvis: Goodbye!")
            break
        reply = ask_jarvis(user_input)
        print(f"Jarvis: {reply}\n")
        speak(reply)
