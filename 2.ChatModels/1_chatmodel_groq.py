from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    # HumanMessage(content="What is the capital of France?"),
    # HumanMessage(content="What about Bihar then?")
    HumanMessage(content="Give 5 nepali female names?")

]

response = llm.invoke(messages)

print(response.content)