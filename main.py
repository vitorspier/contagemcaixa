import streamlit as st
from datetime import datetime

# Função para calcular o total
def calcular_total(moedas, cedulas):
    total_moedas = sum([quantidade * valor for valor, quantidade in moedas.items()])
    total_cedulas = sum([quantidade * valor for valor, quantidade in cedulas.items()])
    return total_moedas, total_cedulas

# Função para formatar valores
def formatar_valor(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Dicionários para armazenar a quantidade de moedas e cédulas
moedas = {0.05: 0, 0.10: 0, 0.25: 0, 0.50: 0, 1.00: 0}
cedulas = {2.00: 0, 5.00: 0, 10.00: 0, 20.00: 0, 50.00: 0, 100.00: 0, 200.00: 0}

st.title("Contagem de Caixa")

# Layout em colunas para moedas
st.header("Moedas")
col1, col2 = st.columns([2, 2])
with col1:
    for valor in [0.05, 0.10, 0.25]:
        moedas[valor] = st.number_input(f"Quantidade de moedas de R${valor:.2f}", min_value=0, step=1)
        st.write(f"Subtotal: R${formatar_valor(moedas[valor] * valor)}")
with col2:
    for valor in [0.50, 1.00]:
        moedas[valor] = st.number_input(f"Quantidade de moedas de R${valor:.2f}", min_value=0, step=1)
        st.write(f"Subtotal: R${formatar_valor(moedas[valor] * valor)}")

# Layout em colunas para cédulas
st.header("Cédulas")
col3, col4 = st.columns([1, 1])
with col3:
    for valor in [2.00, 5.00, 10.00, 20.00]:
        cedulas[valor] = st.number_input(f"Quantidade de cédulas de R${valor:.2f}", min_value=0, step=1)
        st.write(f"Subtotal: R${formatar_valor(cedulas[valor] * valor)}")
with col4:
    for valor in [50.00, 100.00, 200.00]:
        cedulas[valor] = st.number_input(f"Quantidade de cédulas de R${valor:.2f}", min_value=0, step=1)
        st.write(f"Subtotal: R${formatar_valor(cedulas[valor] * valor)}")

# Calcular o total
if st.button("Calcular Total"):
    total_moedas, total_cedulas = calcular_total(moedas, cedulas)
    total = total_moedas + total_cedulas
    st.markdown(f"## Total no caixa: R${formatar_valor(total)}")

    # Gerar histórico
    with open("historico.txt", "a") as file:
        file.write(f"{datetime.now()}: Total no caixa: R${formatar_valor(total)}\n")

# Mostrar histórico
if st.button("Mostrar Histórico"):
    with open("historico.txt", "r") as file:
        historico = file.read()
    st.text_area("Histórico de Consultas", historico)
