from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("{soru}")

chain = prompt | LLM 

print(chain.invoke({"soru": "Merhaba, benim adım Can."}).content)
print(chain.invoke({"soru": "Merhaba, benim adım ne?."}).content)

