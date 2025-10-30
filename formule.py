from langchain_community.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

import google.generativeai as genai

# Set your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load a Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate text
response = model.generate_content("Write 3 sentences in French about Paris.")
print(response.text)
