# Load variables from .env
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Send request to the model
response = client.responses.create(
    model="gpt-6-luna",
    input="Give some good prompts for study"
)

# Display the response
print(response.output_text)