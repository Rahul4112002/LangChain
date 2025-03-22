from openai import OpenAI

client = OpenAI(
    base_url="https://api.sree.shop/v1",
    api_key="ddc-fgUCR5NirIvKjf5kzg7SdP4E0M2sMgmEcQDuK4xNaHTiwDM69F"  # Replace with your API key
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)

