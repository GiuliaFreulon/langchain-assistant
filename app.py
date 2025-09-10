from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

template = """Você é um assitente responsável por ensinar inglês. Explique de maneira didática a dúvida do usuário, fazendo correções, sugestões, traduções e explicações.

Histórico da conversa:
{history}

Entrada do usuário:
{input}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

llm = ChatGroq(temperature=0.7, model="llama-3.3-70b-versatile")

chain = prompt | llm

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def iniciar_assistente():
    print("\nBem-Vindo ao Assistente de Inglês! Digite 'sair' para encerrar.")

    while True:
        pergunta_usuario = input("\nVocê: ")

        if pergunta_usuario.lower() in ["sair", "exit"]:
            print("\nEncerrando o assistente. Até logo!")
            break

        resposta = chain_with_history.invoke(
            {'input': pergunta_usuario},
            config={'configurable': {'session_id': 'user123'}}
        )

        print('\nAssistente: ', resposta.content)

if __name__ == "__main__":
    iniciar_assistente()