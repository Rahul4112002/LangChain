#openai query
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings( 
                api_key=api_key,
                model='text-embedding-3-large', 
                dimensions=32,
                openai_api_base="https://api.sree.shop/v1")

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))