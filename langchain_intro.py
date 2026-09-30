from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate.from_template("Bana {subject} ile yapılan bir tatlı ismi öner.")

chain = prompt | LLM

result = chain.invoke({"subject": "Çilek"})

print(result.content)

