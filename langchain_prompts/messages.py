from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content = "Tell me about Langhain")
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(messages)