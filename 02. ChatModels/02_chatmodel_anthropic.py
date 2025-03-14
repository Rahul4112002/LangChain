from langchain_anthropic import ChatAnthropic 
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.4-sonnet')

result = model.invoke("what is capital of India?")

print(result.content)