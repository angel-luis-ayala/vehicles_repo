import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos

st.header("Ventas de vehículos")  # Crear encabezado

# Crear casilla de verificación
hist_checkbox = st.checkbox('Construir histograma')

if hist_checkbox:  # Si se selecciona la casilla...
    # escribir un mensaje
    st.write('Creación de un histograma para el kilometraje de los autos')

    # crear el histograma
    fig = px.histogram(car_data, x='odometer',
                       title='Distribución de kilometraje')

    # mostrarlo en modo interactivo
    st.plotly_chart(fig, use_container_width=True)


# Crear casilla de verificación
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

if scatter_checkbox:  # Si se selecciona la casilla...
    # escribir un mensaje
    st.write('Gráfico de dispersión: Kilometraje vs Precio de autos')

    # crear el gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Relación entre kilometraje y precio')

    # mostrarlo en modo interactivo
    st.plotly_chart(fig, use_container_width=True)
