from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import os
load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give sentiment of the feedback')

pydanticparser = PydanticOutputParser(pydantic_object=Feedback)
model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Classift the sentiment of the following feedback into positive or negative\n {text} \n {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction':pydanticparser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydanticparser

# result = classifier_chain.invoke({'text':'not upto to the mark product'})

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n, {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n, {feedback}',
    input_variables=['feedback']
)


branch_chain = RunnableBranch(
    #template
    # (condition1, chain1),
    # (condition2, chain2),
    # default chain

    # lambda parameter : expression

    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
    
)

chain = classifier_chain | branch_chain
result = chain.invoke({'text':'worth it to invest in'})

print(result)

chain.get_graph().print_ascii()