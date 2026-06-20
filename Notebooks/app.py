import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('car_data.csv')
st.header('Car Data Analysis / Proyecto Sprint 7')

graph_button = st.button('Construir gráficos')

if graph_button:
    st.write(
        'Creación de gráficos para el conjunto de datos de automóviles americanos.')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
