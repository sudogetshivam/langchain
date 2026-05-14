from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt=18, description='Age of the person')
    dob : str = Field(description='date of birth of that person')
    city : str = Field(description='Name of the city person belongs too')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= 'Generate the name,age,date of birth and city of a fictional {place} person \n {format_instruction}',
    input_variables=['places'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

#chain method
chain = template | model | parser

result = chain.invoke({'place':'nepal'})

print(result)