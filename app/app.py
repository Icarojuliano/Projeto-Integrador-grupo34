elif pagina == "Gráficos Simples":
    # Distribuição da área plantada
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
