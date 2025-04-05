from langchain.prompts import ChatPromptTemplate
from .models import get_llm_model
from .prompts import get_chat_prompt
from .data_processor import DataProcessor
import os

class ChatAgent:
    """
    Agente de chat que processa mensagens e gera respostas com base em dados.
    """
    
    def __init__(self, temperature=0.7, csv_path=None):
        """
        Inicializa o agente de chat.
        
        Args:
            temperature: Controla a aleatoriedade das respostas
            csv_path: Caminho para o arquivo CSV de dados (opcional)
        """
        self.llm = get_llm_model(temperature=temperature)
        self.data_processor = DataProcessor(csv_path)
        self.prompt = get_chat_prompt()
        # Nova sintaxe usando pipe operator (|) em vez de LLMChain
        self.chain = self.prompt | self.llm
    
    def set_csv_data(self, csv_path):
        """
        Define o arquivo CSV para o agente usar.
        
        Args:
            csv_path: Caminho para o arquivo CSV
            
        Returns:
            Boolean indicando sucesso
        """
        if not os.path.exists(csv_path):
            return False
        return self.data_processor.load_data(csv_path)
    
    async def process_message(self, message):
        """
        Processa uma mensagem do usuário e retorna a resposta.
        
        Args:
            message: Mensagem do usuário
            
        Returns:
            Resposta gerada pelo modelo
        """
        # Obter dados relevantes do CSV para contextualizar a resposta
        context_data = {}
        
        # Se tivermos dados carregados, fazer consulta básica
        if self.data_processor.data is not None:
            context_data = self.data_processor.query_data(message)
        
        # Adiciona o contexto à mensagem
        enhanced_message = {
            "input": message,
            "data_context": str(context_data)
        }
        
        # Invoca o modelo com a mensagem aprimorada
        response = await self.chain.ainvoke(enhanced_message)
        return response.content
