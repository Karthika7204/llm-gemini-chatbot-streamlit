from google import genai
client = genai.Client(api_key="AIzaSyAsg7riggyVzrw2TH_4xgp1V2vygxOIado")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)
