from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini")
# prompt = ChatPromptTemplate.from_template("{question}")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sen yardımsever bir asistansın."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | LLM 

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    return SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///history.db"
    )

chain_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "can1"}}

#response1 = chain_memory.invoke(
#    {"question": "Merhaba, benim adım Can Python öğreniyorum"},
#    config=config
#)

response2 = chain_memory.invoke(
    {"question": "Merhaba, benim adım ne ve ne öğreniyorum?"},
    config=config
)

print(f"response 2: {response2.content}")

