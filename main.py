import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

convo_history = [
    {
        "role":"system",
        "content":"You are a software engineer assistant"
    }
]

print("AI Chatbot initialized (type 'quit' to exit)")

while True:
    user_input=input("\nyou: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit","exit","q"]:
        print("Chatbot: Goodbye!")
        break


    convo_history.append({"role":"user","content":user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=convo_history,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print(f"\nAi: {reply}")

        convo_history.append({"role":"assistant","content":reply})
    except Exception as e:
        print(f"Error: {e}")