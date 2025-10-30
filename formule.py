from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM (you can replace with ChatOpenAI if you use GPT-4)
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a simple prompt
prompt = PromptTemplate(
    input_variables=[],
    template="Écris trois phrases simples en français."
)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.run()
print(response)
