from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

model = GoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke("What is the capital of Nepal?")

print(result.content)
