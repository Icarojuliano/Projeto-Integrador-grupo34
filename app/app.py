#app.py
import streamlit as st
import pandas as pd

# Título principal
st.title("data/raw/pam_sintetico_multiculturas_50k.csv")

# Carregar dados da pasta "dados"
df = pd.read_csv("data/raw/pam_sintetico_multiculturas_50k.csv")

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
