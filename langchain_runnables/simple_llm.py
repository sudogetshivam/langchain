from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

prompt = PromptTemplate(
    input_variables=['topic'],
    template='suggest a catchy blog title about {topic}'
)

topic = input('Enter a topic: ')

formatted_prompt = prompt.format(topic=topic)

title = model.invoke(formatted_prompt)

print("Generated Blog title is: \n",title)