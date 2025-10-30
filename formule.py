from langchain_community.llms import OpenAI
import os
from print import info, error, success
from prompts import Prompts
from dotenv import load_dotenv

#from openai import OpenAI

import google.generativeai as genai
load_dotenv()
# Configure Gemini with API key from .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
info("-----------  Loading  ------------")
model = genai.GenerativeModel("models/gemini-2.5-flash")

info('-----------      --------------')
text = input("Add you're sentence here: ")
info(text)
prompt =Prompts.manieres
full_prompt = prompt + " " + text
error(full_prompt)
    

try:

    tokens_info = model.count_tokens(full_prompt)
    info(f"Estimated input tokens: {tokens_info.total_tokens}")
except Exception as e:
    error(f"count_tokens not supported: {e}")

response = model.generate_content(full_prompt)
success(f"Output:\n{response.text}")