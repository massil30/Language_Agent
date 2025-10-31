import os
from print import info, error, success
from prompts import Prompts
from dotenv import load_dotenv

#from openai import OpenAI
from langchain_community.llms import OpenAI
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
#from langchain.schema import SystemMessage, HumanMessage

#Load Api Key
load_dotenv()
# Configure Gemini with API key from .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
info("-----------  Loading  ------------")
model = genai.GenerativeModel("models/gemini-2.5-flash")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers in French with short answers no extra explanation. "),
    ("human", "{question}")
])
info('--------------------------------------')
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
#print(f"\n🧠 Response:")
success(f"Output:\n{response.text}")