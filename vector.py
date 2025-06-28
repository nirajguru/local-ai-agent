from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model = "mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)
''' ChromadB
https://docs.trychroma.com/docs/overview/getting-started


'''