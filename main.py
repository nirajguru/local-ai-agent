from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="mistral:7b")

template = """
You are an expert in answering questions about a pizza restaurant.
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("Ask your question (q to quit): ")
    print("\n")
    if question == "q":
        break 
    result = chain.invoke({"reviews": [],
              "question": question})
    print(result) 