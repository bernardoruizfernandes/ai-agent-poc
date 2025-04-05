from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

def get_llm_model(temperature=0.7):
    """
    Configura e retorna uma instância do modelo Gemini.
    
    Args:
        temperature: Controla a aleatoriedade das respostas (0.0 a 1.0)
        
    Returns:
        Uma instância do modelo Gemini configurada
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY não encontrada nas variáveis de ambiente")
    
    # Configura o modelo Gemini - com nome correto do modelo
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",  # Atualizado de gemini-pro para gemini-1.5-pro
        google_api_key=api_key,
        temperature=temperature,
        convert_system_message_to_human=False  # Alterado para False para evitar o aviso de depreciação
    )
    
    return llm
