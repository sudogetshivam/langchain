from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os
load_dotenv()


model1 = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

model2 = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

prompt1 = PromptTemplate(
    template='Genrate notes on this {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate quiz of  5 questios on this {topic},',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser =  StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser , #notes is our chain
    'quiz' : prompt2 | model2 | parser
}
)

merge_chain = prompt3 | model2 | parser
chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification,
regression and outliers detection.

The advantages of support vector machines are:

· Effective in high dimensional spaces.
· Still effective in cases where number of dimensions is greater than the number of samples.
. Uses a subset of training points in the decision function (called support vectors), so it is also memory
efficient.

· Versatile: different Kernel functions can be specified for the decision function. Common kernels are
provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

. If the number of features is much greater than the number of samples, avoid over-fitting in choosing
Kernel functions and regularization term is crucial.
· SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold
cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by
numpy.asarray) and sparse (any scipy. sparse) sample vectors as input. However, to use an SVM to make
predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered
humpy.ndarray (dense) or scipy. sparse. csr_matrix (sparse) with dtype=float64
tial Choin
"""

result = chain.invoke({'topic':text})
# print(result)
chain.get_graph().print_ascii()