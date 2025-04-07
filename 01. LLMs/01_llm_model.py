# this is llm langchain
from langchain_openai import ChatOpenAI  # Changed to ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Use ChatOpenAI instead of OpenAI
llm = ChatOpenAI(
    api_key=api_key,
    model='gpt-4o',
    openai_api_base="https://api.sree.shop/v1"  # Custom endpoint
)

# Invoke the model
result = llm.invoke("What is the capital of India?")

# Print result
print(result.content)
