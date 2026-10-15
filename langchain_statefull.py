from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini")
# prompt = ChatPromptTemplate.from_template("{soru}")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sen yardımsever bir asistansın."),
    MessagesPlaceholder(variable_name="gecmis"),
    ("human", "{soru}")
])

chain = prompt | LLM 

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()

    return store[session_id]

chain_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="soru",
    history_messages_key="gecmis"
)

config = {"configurable": {"session_id": "can1"}}

response1 = chain_memory.invoke(
    {"soru": "Merhaba, benim adım Can Python öğreniyorum"},
    config=config
)

response2 = chain_memory.invoke(
    {"soru": "Merhaba, benim adım ne ve ben ne öğreniyorum?"},
    config=config
)

print(f"response 1: {response1.content}")
print("-"*60)
print(f"response 2: {response2.content}")


