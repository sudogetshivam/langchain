from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from typing import TypedDict,Annotated

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

#schema
class Review(TypedDict):
    summary:Annotated[str,"A breif summary of review"]
    sentiment:Annotated[str,"return sentiment of the review either positive,negative or neutral"]

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks qutdated compared to other brands. Hoping for a software update to fix this.")

print(response)
