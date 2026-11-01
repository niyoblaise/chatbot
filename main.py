import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a software engineer assistant",
        temperature=0.7,
    )
)

print("AI Chatbot initialized (type 'quit' to exit)")

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Chatbot: Goodbye!")
        break

    try:
        # chat.send_message automatically manages and appends to conversation history
        response = chat.send_message(user_input)
        print(f"\nAI: {response.text}")

    except Exception as e:
        print(f"Error: {e}")