import streamlit as st
from fuzzywuzzy import fuzz
import time


st.set_page_config(
    page_title="mozango",
    page_icon="💖",
    layout="wide"
    )
# Função para ler e pré-processar os dados do arquivo
def ler_dados_arquivo(arquivo):
    with open(arquivo, "r", encoding="latin-1") as file:
        linhas = file.readlines()
    pares_de_dialogo = [linha.strip().split("/") for linha in linhas]
    return pares_de_dialogo

# Função para encontrar a pergunta mais semelhante no arquivo de treinamento
def encontrar_pergunta_similar(user_input, pares_de_dialogo):
    max_similarity = 0
    resposta = None

    for pergunta, resp in pares_de_dialogo:
        similarity = fuzz.ratio(user_input.lower(), pergunta.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            resposta = resp

    return resposta

# Título do chatbot
st.title("Lalove💝Anlovi")

# Introdução
st.markdown("**Olá! Estou aqui para ajudar. Pergunte-me qualquer coisa sobre vocês!**")

# Campo de entrada de texto para a pergunta do usuário
user_input = st.text_input("Você: ")

# Opção para carregar dados de treinamento de um arquivo
treinar_com_arquivo = st.checkbox("Treinar com Dados de Arquivo")

# Botão para enviar a pergunta
if st.button("Enviar"):
    user_input = user_input.strip()  # Remova espaços em branco em excesso
    response = None

    # Se a opção de treinamento com arquivo estiver marcada
    if treinar_com_arquivo:
        # Leia e pré-processe os dados do arquivo
        pares_de_dialogo = ler_dados_arquivo("ME1.txt")

        # Simula um atraso para mostrar que o chatbot está pensando
        with st.spinner("Pensando..."):
            time.sleep(2)  # Simulando 2 segundos de pensamento

            response = encontrar_pergunta_similar(user_input, pares_de_dialogo)

        st.success("Processamento concluído!")

        if response:
            st.write("Resposta do Chatbot:")
            st.write(response)
        else:
            st.write("Pergunta não encontrada no arquivo. Eu fui limitado a dar respostas que estão no arquivo do meu treinamento para previnir respostas indesejadas.")
    else:
        # Resposta padrão se a opção de treinamento com arquivo não estiver marcada
        st.markdown("**Opção *Treinar com Dados de Arquivo* não marcada. Por favor, marque a opção e tente novamente.**")

# Nota sobre o chatbot
st.info("Este é um chatbot treinado com base na correspondência de dados de **Anlovi** e **Lalovi**.")
