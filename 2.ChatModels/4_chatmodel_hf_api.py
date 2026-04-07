from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),  # uncomment kar
    #pata hain es line ke bina bhi chaljayega
    #Tera token .env mein HUGGINGFACEHUB_API_TOKEN ke naam se pada hai
    # load_dotenv() us token ko environment mein load kar deta hai, aur HuggingFaceEndpoint automatically 
    # usse pick kar leta hai even if tu explicitly pass nahi karta constructor mein.
    
    task="conversational",
    max_new_tokens=100,
    temperature=0.5,
    provider="auto",
)

chat = ChatHuggingFace(llm=llm)
result = chat.invoke("What is the capital of India?")
print(result.content)