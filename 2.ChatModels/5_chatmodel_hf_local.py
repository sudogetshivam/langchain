from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    model_id = "meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.5},

)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")