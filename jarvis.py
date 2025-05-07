# jarvis.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Endpoint and model
api_url = "https://openrouter.ai/api/v1/chat/completions"
model = "mistralai/mistral-7b-instruct"  # You can change this to other free models

def ask_jarvis(prompt):
    """
    Send prompt to OpenRouter API and return response.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourapp.com",  # Required, just put your project name if no site
        "X-Title": "jarvis-assistant"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful and intelligent assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main loop
if __name__ == "__main__":
    print("Jarvis (OpenRouter) is online. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Jarvis: Goodbye!")
            break
        reply = ask_jarvis(user_input)
        print(f"Jarvis: {reply}\n")
