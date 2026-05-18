from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('FinalReport.pdf')

# docs = loader.load()


text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to
exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to
advancements in technology here on Earth. Satellite communications, GPS, and even certain medical
imaging techniques trace their roots back to innovations driven by space programs.
"""

spillter =  RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)

chunks = spillter.split_text(text)

print(len(chunks))
print(chunks)
# result = spillter.split_documents(docs)
# print(len(result[0].page_content))