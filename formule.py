from langchain_community.llms import OpenAI
import os
from print import info, error, success

from dotenv import load_dotenv

#from openai import OpenAI

import google.generativeai as genai
load_dotenv()
# Configure Gemini with API key from .env file
genai.configure(api_key='-QY')
info("-----------  Loading  ------------")
model = genai.GenerativeModel("models/gemini-2.5-flash")

prompt = "Écris trois phrases en français sur Paris"

    

try:
    error("test error message")

    tokens_info = model.count_tokens(prompt)
    info(f"Estimated input tokens: {tokens_info.total_tokens}")
except Exception as e:
    error(f"count_tokens not supported: {e}")

response = model.generate_content(prompt)
success(f"Output:\n{response.text}")