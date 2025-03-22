from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model='gpt-4o',
    openai_api_base="https://api.sree.shop/v1"  # Custom endpoint
)


result = model.invoke("what is capital of India?")

print(result.content)