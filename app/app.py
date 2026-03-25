#app.py
import streamlit as st
import pandas as pd

# Título principal
st.title("Dashboard - Projeto Integrador Grupo 34")

# Carregar dados da pasta "dados"
df = pd.read_csv("dados/usuarios.csv")

# Exibir tabela
st.subheader("Tabela de Usuários")
st.dataframe(df)

# Estatísticas básicas
st.subheader("Estatísticas Básicas")
st.write(df.describe())

# Exemplo de gráfico simples (opcional)
if "idade" in df.columns:
    st.subheader("Distribuição de Idades")
    st.bar_chart(df["idade"])
