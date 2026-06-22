import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# Configuración de la página
# =========================

st.set_page_config(
    page_title="Sprint 7 - Proyecto Análisis de Datos de Automóviles",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Experimentando con la documentación de Streamlit para crear una aplicación interactiva de análisis de datos de automóviles."
    }
)

# =========================
# Cargar y tratar los datos
# =========================

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
car_filtered = car_data.groupby(['model_year', 'model'])['price'].mean(
).reset_index()  # agrupar por modelo y año, y calcular el precio promedio

# =========================
# Título principal
# =========================
st.title("🚗 Car Data Analysis — Proyecto Sprint 7")
st.write("Análisis interactivo del dataset de automóviles americanos.")


st.header('Análisis de datos de automóviles americanos. Vista previa del dataset')
with st.expander("📄 Ver primeras filas del dataset"):
    st.dataframe(car_data.head())  # mostrar las primeras filas del DataFrame

agree = st.checkbox(
    "¿Quieres ver la distribución de transmisiones?")
if agree:
    st.write("---")
    st.write("Creación de histogramas para el conjunto de datos de automóviles americanos automáticos vs estandar.")
    car_hist = car_data['transmission'].hist(
        bins=50)  # crear un histograma con 50 bins
    st.pyplot(car_hist.figure)  # mostrar el histograma en Streamlit


graph_line_button = st.button('Construir gráficos de líneas')

if graph_line_button:
    st.write('---')
    st.write(
        'Creación de gráficos lineales para el conjunto de datos de automóviles americanos.')
    fig = px.line(car_filtered, x="model_year", y="price", color="model")
    st.plotly_chart(fig, use_container_width=True)

graph_scatter_button = st.button('Construir gráficos scatter')

if graph_scatter_button:
    st.write('---')
    st.write(
        'Creación de gráficos scatter para el conjunto de datos de automóviles americanos.')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig, use_container_width=True)
