from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

while True:
    user_input = input("You: ") 
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)
