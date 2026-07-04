from google import genai

client = genai.Client(api_key="your_API_key")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Artificial Intelligence?"
)

print(response.text)