import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# Configuración de la página
# =========================
st.set_page_config(
    page_title="Car Data Analysis",
    page_icon="🚗",
    layout="wide"
)

# =========================
# Carga de datos
# =========================


@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")


car_data = load_data()

# =========================
# Título principal
# =========================
st.title("🚗 Car Data Analysis — Proyecto Sprint 7")
st.write("Análisis interactivo del dataset de automóviles americanos.")

# =========================
# Vista previa de datos
# =========================
with st.expander("📄 Ver primeras filas del dataset"):
    st.dataframe(car_data.head())

# =========================
# Checkbox para histogramas
# =========================
st.subheader("Distribución de Transmisiones")

if st.checkbox("Mostrar histograma de transmisiones"):
    st.write("Histograma de transmisiones automáticas vs estándar.")
    fig_hist = px.histogram(car_data, x="transmission", nbins=50)
    st.plotly_chart(fig_hist, use_container_width=True)

# =========================
# Gráfico de líneas
# =========================
st.subheader("Precio promedio por año y modelo")

car_filtered = (
    car_data.groupby(["model_year", "model"])["price"]
    .mean()
    .reset_index()
)

if st.button("Construir gráfico de líneas"):
    fig_line = px.line(
        car_filtered,
        x="model_year",
        y="price",
        color="model",
        title="Precio promedio por año y modelo"
    )
    st.plotly_chart(fig_line, use_container_width=True)

# =========================
# Gráfico scatter
# =========================
st.subheader("Relación entre año del modelo y precio")

if st.button("Construir gráfico scatter"):
    fig_scatter = px.scatter(
        car_data,
        x="model_year",
        y="price",
        opacity=0.6,
        title="Scatter: Año del modelo vs Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
