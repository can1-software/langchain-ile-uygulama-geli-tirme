from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini")
# prompt = ChatPromptTemplate.from_template("{soru}")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sen yardımsever bir asistansın."),
    MessagesPlaceholder(variable_name="gecmis"),
    ("human", "{soru}")
])

chain = prompt | LLM 

print(chain.invoke({"soru": "Merhaba, benim adım Can."}).content)
print(chain.invoke({"soru": "Merhaba, benim adım ne?."}).content)



