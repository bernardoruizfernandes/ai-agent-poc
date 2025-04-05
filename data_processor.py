import pandas as pd
import os

class DataProcessor:
    """
    Classe para processar e consultar dados de CSV para o agente.
    """
    
    def __init__(self, csv_path=None):
        """
        Inicializa o processador de dados.
        
        Args:
            csv_path: Caminho para o arquivo CSV (opcional)
        """
        self.data = None
        if csv_path and os.path.exists(csv_path):
            self.load_data(csv_path)
    
    def load_data(self, csv_path):
        """
        Carrega dados de um arquivo CSV.
        
        Args:
            csv_path: Caminho para o arquivo CSV
        
        Returns:
            Boolean indicando sucesso
        """
        try:
            self.data = pd.read_csv(csv_path)
            return True
        except Exception as e:
            print(f"Erro ao carregar o CSV: {e}")
            return False
    
    def get_data_summary(self):
        """
        Retorna um resumo dos dados carregados.
        
        Returns:
            String com resumo dos dados ou mensagem de erro
        """
        if self.data is None:
            return "Nenhum dado carregado."
        
        summary = {
            "linhas": len(self.data),
            "colunas": list(self.data.columns),
            "tipos_dados": {col: str(dtype) for col, dtype in self.data.dtypes.items()}
        }
        
        return summary
    
    def query_data(self, query_text):
        """
        Executa consultas simples nos dados baseadas em texto.
        
        Args:
            query_text: Descrição da consulta em texto natural
            
        Returns:
            Resultado da consulta ou mensagem informativa
        """
        if self.data is None:
            return "Nenhum dado carregado para consulta."
        
        try:
            # Dependendo da complexidade da sua consulta, você pode implementar
            # lógica mais sofisticada aqui. Esta é uma implementação básica.
            
            # Exemplo básico: se for sobre estatísticas gerais
            if "estatística" in query_text.lower() or "resumo" in query_text.lower():
                return self.data.describe().to_dict()
            
            # Exemplo: se for sobre valores únicos em uma coluna
            for col in self.data.columns:
                if col.lower() in query_text.lower() and ("único" in query_text.lower() or "diferentes" in query_text.lower()):
                    return {"valores_unicos": self.data[col].unique().tolist()}
            
            # Retorno padrão: primeiras linhas dos dados
            return self.data.to_dict(orient='records')
            
        except Exception as e:
            return f"Erro ao consultar dados: {e}"