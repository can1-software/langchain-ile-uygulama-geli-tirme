from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

parser = CommaSeparatedListOutputParser()

format_intructions = parser.get_format_instructions() # liste halinde almak için
prompt = ChatPromptTemplate.from_template("Bana {fruit} ile yapılan 5 tatlı ismi ver. \n{format_intructions}")
prompt = prompt.partial(format_intructions=format_intructions)

# LCEL ("|") (LangChain Expression Language) # Bu bir kavram
chain = prompt | LLM | parser

result = chain.invoke({"fruit": "Çilek"})

print(result)

