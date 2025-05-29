### can change the embedding to the cloud
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import BedrockEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    #embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return embeddings