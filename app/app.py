import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ==============================
# Título principal
# ==============================
st.title("Dashboard - Projeto Integrador Grupo 34")

# ==============================
# Carregar dados
# ==============================
df = pd.read_csv("dados/usuarios.csv")

# ==============================
# Barra lateral de navegação
# ==============================
pagina = st.sidebar.radio(
    "Navegação",
    ["Tabela", "Estatísticas", "Gráficos Simples", "Gráficos Interativos"]
)

# ==============================
# Página: Tabela
# ==============================
if pagina == "Tabela":
    st.subheader("Tabela de Usuários")
    st.dataframe(df)

# ==============================
# Página: Estatísticas
# ==============================
elif pagina == "Estatísticas":
    st.subheader("Estatísticas Básicas")
    st.write(df.describe(include="all"))

    # Estatísticas por grupo (se existir coluna 'cidade')
    if "cidade" in df.columns:
        st.subheader("Média de idade por cidade")
        st.write(df.groupby("cidade")["idade"].mean())

# ==============================
# Página: Gráficos Simples
# ==============================
elif pagina == "Gráficos Simples":
    if "idade" in df.columns:
        st.subheader("Distribuição de Idades")
        st.bar_chart(df["idade"])

    # Histograma com Matplotlib
    if "idade" in df.columns:
        fig, ax = plt.subplots()
        ax.hist(df["idade"], bins=10, color="skyblue", edgecolor="black")
        ax.set_title("Histograma de Idades")
        ax.set_xlabel("Idade")
        ax.set_ylabel("Frequência")
        st.pyplot(fig)

# ==============================
# Página: Gráficos Interativos
# ==============================
elif pagina == "Gráficos Interativos":
    coluna = st.selectbox("Selecione uma coluna para análise:", df.columns)

    st.subheader(f"Distribuição de {coluna}")
    fig = px.histogram(df, x=coluna, nbins=20, title=f"Distribuição de {coluna}")
    st.plotly_chart(fig)

    # Se houver duas colunas numéricas, permitir scatter plot
    num_cols = df.select_dtypes(include="number").columns
    if len(num_cols) >= 2:
        x_axis = st.selectbox("Selecione eixo X:", num_cols)
        y_axis = st.selectbox("Selecione eixo Y:", num_cols)
        st.subheader(f"Relação entre {x_axis} e {y_axis}")
        fig2 = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[0])
        st.plotly_chart(fig2)

