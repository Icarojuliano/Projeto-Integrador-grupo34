
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
df = pd.read_csv("data/raw/pam_sintetico_multiculturas_50k.csv")

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
    st.subheader("Tabela de Dados")
    st.dataframe(df)

# ==============================
# Página: Estatísticas
# ==============================
elif pagina == "Estatísticas":
    st.subheader("Estatísticas Simplificadas")

    # Cards com métricas principais (em colunas)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Área média (ha)", round(df["area_plantada_ha"].mean(), 2))
    col2.metric("Precipitação média (mm)", round(df["precipitacao_mm"].mean(), 2))
    col3.metric("Temperatura média (°C)", round(df["temp_media_c"].mean(), 2))
    col4.metric("Rendimento médio (kg/ha)", round(df["rendimento_kg_ha"].mean(), 2))

    # Ranking de municípios
    st.subheader("Top 5 Municípios por Área Plantada")
    top_municipios = (
        df.groupby("municipio")["area_plantada_ha"]
          .sum()
          .sort_values(ascending=False)
          .head(5)
          .reset_index()
    )
    st.bar_chart(top_municipios.set_index("municipio"))

    # Tendência por ano
    st.subheader("Resumo por Ano")
    resumo_ano = df.groupby("ano")[["area_plantada_ha","rendimento_kg_ha"]].mean().reset_index()
    fig = px.line(resumo_ano, x="ano", y=["area_plantada_ha","rendimento_kg_ha"],
                  labels={"value":"Média","variable":"Indicador"})
    st.plotly_chart(fig)

# ==============================
# Página: Gráficos Simples
# ==============================
elif pagina == "Gráficos Simples":
    # Bar chart da área plantada
    st.subheader("Distribuição da Área Plantada")
    st.bar_chart(df["area_plantada_ha"])

    # Histograma da precipitação
    st.subheader("Histograma da Precipitação")
    fig, ax = plt.subplots()
    ax.hist(df["precipitacao_mm"], bins=20, color="skyblue", edgecolor="black")
    ax.set_title("Distribuição da Precipitação")
    ax.set_xlabel("Precipitação (mm)")
    ax.set_ylabel("Frequência")
    st.pyplot(fig)

    # Histograma da temperatura média
    st.subheader("Histograma da Temperatura Média")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["temp_media_c"], bins=20, color="lightgreen", edgecolor="black")
    ax2.set_title("Distribuição da Temperatura Média")
    ax2.set_xlabel("Temperatura (°C)")
    ax2.set_ylabel("Frequência")
    st.pyplot(fig2)

    # Histograma do rendimento
    st.subheader("Histograma do Rendimento (kg/ha)")
    fig3, ax3 = plt.subplots()
    ax3.hist(df["rendimento_kg_ha"], bins=20, color="orange", edgecolor="black")
    ax3.set_title("Distribuição do Rendimento")
    ax3.set_xlabel("Rendimento (kg/ha)")
    ax3.set_ylabel("Frequência")
    st.pyplot(fig3)

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
        fig2 = px.scatter(df, x=x_axis, y=y_axis, color="municipio")
        st.plotly_chart(fig2)
