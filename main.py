
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from .env")

if not model:
    raise ValueError("GROQ_MODEL is missing from .env")

client = Groq(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are a software engineer assistant"
    }
]

print(f"AI Chatbot initialized using {model} (type 'quit' to exit)")

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        ai_response = response.choices[0].message.content

        print(f"\nAI: {ai_response}")

        messages.append({
            "role": "assistant",
            "content": ai_response
        })

    except Exception as e:
        print(f"Error: {e}")
        messages.pop()
