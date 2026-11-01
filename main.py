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