import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
car_data.head()  # mostrar las primeras filas del DataFrame
car_filtered = car_data.groupby(['model_year', 'model'])['price'].mean(
).reset_index()  # agrupar por modelo y año, y calcular el precio promedio
car_filtered.head()  # mostrar las primeras filas del DataFrame filtrado

st.header('Car Data Analysis / Proyecto Sprint 7')

agree = st.checkbox(
    "Bienvenido al proyecto de análisis de datos de automóviles! ¿Quieres explorar los datos y visualizarlos?")

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
