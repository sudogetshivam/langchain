import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5.4-nano",
    input="Hello"
)

print(response.output[0].content[0].text)