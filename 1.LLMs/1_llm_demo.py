from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0  # Optional: keeps responses consistent
)

# 3. Invoke the model
try:
    response = llm.invoke("what is the capital of France?")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
