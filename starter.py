import chainlit as cl

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Análise de picos de recarga",
            message="Poderia analisar os horários de pico nas recargas dos veículos elétricos para otimização da operação?",
            icon="",  # Você pode usar emojis diretamente se preferir
        ),
        cl.Starter(
            label="Consumo por posto",
            message="Quais são os postos com maior consumo energético na nossa rede? Preciso de uma comparação.",
            icon="",
        ),
        cl.Starter(
            label="Relatório mensal",
            message="Gere um relatório de uso mensal dos postos de recarga com as principais métricas e tendências.",
            icon="",
        ),
        cl.Starter(
            label="Perfil de clientes",
            message="Analise o comportamento dos nossos usuários mais frequentes e seus padrões de recarga.",
            icon="",
        )
    ]