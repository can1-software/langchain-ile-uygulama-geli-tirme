from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# prompt = ChatPromptTemplate.from_template("Bana {fruit} ile yapılan bir tatlı ismi öner.")
prompt = ChatPromptTemplate.from_messages([
    ("system", ""),
    ("human", "")
])

# LCEL ("|") (LangChain Expression Language) # Bu bir kavram
chain = prompt | LLM

result = chain.invoke({"fruit": "Çilek"})

print(result.content)
