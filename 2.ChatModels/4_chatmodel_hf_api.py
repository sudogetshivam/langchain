from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Token can be provided in multiple ways:
# 1. Constructor mein diya token (api_token parameter)
# 2. HUGGINGFACEHUB_API_TOKEN env var
# 3. HF_TOKEN env var
# 4. ~/.cache/huggingface/token (CLI login)
# 5. HUGGINGFACE_TOKEN env var

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),  # uncomment kar
    #pata hain es line ke bina bhi chaljayega
    
    task="conversational",
    max_new_tokens=100,
    temperature=0.5,
    provider="auto",
)

chat = ChatHuggingFace(llm=llm)
result = chat.invoke("What is the capital of India?")
print(result.content)