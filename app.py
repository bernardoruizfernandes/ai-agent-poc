import chainlit as cl
from src.agent import ChatAgent
import starter
import os

# Caminho para o arquivo CSV de dados
# Substitua pelo caminho real do seu arquivo CSV
CSV_PATH = "dados/recargas_veiculos.csv"  # Ajuste para o caminho real do seu arquivo

# Inicializa o agente
agent = None

@cl.on_chat_start
async def on_chat_start():
    """Inicializa o agente quando uma nova sessão de chat começa."""
    global agent
    
    # Verifica se o arquivo CSV existe
    csv_exists = os.path.exists(CSV_PATH)
    
    # Inicializa o agente com o CSV se disponível
    agent = ChatAgent(temperature=0.7, csv_path=CSV_PATH if csv_exists else None)
    

@cl.on_message
async def on_message(message: cl.Message):
    """Processa cada mensagem recebida e envia uma resposta."""
    if not agent:
        # Caso o agente não tenha sido inicializado
        await cl.Message(content="Erro: Agente não inicializado. Por favor, recarregue a página.").send()
        return
    
    # Processa a mensagem com o agente
    response = await agent.process_message(message.content)
    
    # Envia a resposta de volta para o usuário
    await cl.Message(content=response).send()