"""
CodeHub Universal Chatbot Framework
-----------------------------------
An open-source chatbot base for developers.

Users can copy, modify, and extend this project
to create their own local or online chatbot apps.

Author: 𝓧𝔂𝓡𝓸𝓷𝓔𝔁 | 𝓓𝓔𝓥
GitHub: https://github.com/filmshadow89-droid/CodeHub
"""

import time

# -----------------------------
# Basic Console Chat System
# -----------------------------
def console_chat():
    print("\n🤖 Welcome to CodeHub Console Chat!")
    print("Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Bot: Goodbye, developer 👋")
            break
        else:
            print("Bot:", generate_response(user_input))

def generate_response(text):
    # Simple text-based logic (customize this)
    responses = {
        "hi": "Hey there 👋! Welcome to CodeHub Chat.",
        "help": "You can extend this chatbot with your own commands in generate_response().",
        "code": "Try exploring the /modules folder for examples!",
        "who made you": "I was created by 𝓧𝔂𝓡𝓸𝓷𝓔𝔁 | 𝓓𝓔𝓥 and the CodeHub community 💻",
    }
    return responses.get(text.lower(), "That's interesting! Tell me more.")

# -----------------------------
# Placeholder for Web Version
# -----------------------------
def web_chat_placeholder():
    print("\n🌐 Web Chat mode coming soon!")
    print("Developers can add a Flask-based chatbot in /web/app.py")

# -----------------------------
# Custom Extensions
# -----------------------------
def run_custom():
    print("\n🧩 Custom mode — extend this section for APIs, AI, or integrations!")

# -----------------------------
# Main Menu
# -----------------------------
def main():
    print("""
  ╔══════════════════════════════════════╗
  ║         CodeHub Chatbot Engine       ║
  ╠══════════════════════════════════════╣
  ║ 1. 🖥️  Console Chat                  ║
  ║ 2. 🌐  Web Chat (Flask Template)     ║
  ║ 3. ⚙️  Custom Extension Mode          ║
  ║ 4. ❌  Exit                          ║
  ╚══════════════════════════════════════╝
    """)

    while True:
        choice = input("Select mode (1-4): ").strip()
        if choice == "1":
            console_chat()
        elif choice == "2":
            web_chat_placeholder()
        elif choice == "3":
            run_custom()
        elif choice == "4":
            print("\n👋 Thanks for using CodeHub Framework!")
            time.sleep(1)
            break
        else:
            print("❗ Invalid choice — try again!")

if __name__ == "__main__":
    main()
