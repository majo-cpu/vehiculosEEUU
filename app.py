import streamlit as st
import pandas as pd
import plotly.express as px
import win32api
car_data = pd.read_csv(r'C:\Users\nicol\OneDrive\Escritorio\vehicles_env\vehicles_us.csv', sep=',')
print(car_data)

# Display the DataFrame (optional)
st.write(car_data)

# Create a button for building the histogram
hist_button = st.button('Construir histograma')

# Check if the button is clicked
if hist_button:
    # Display a message indicating the histogram creation
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Create a histogram using Plotly Express
    fig = px.histogram(car_data, x="odometer")
    
    # Display the Plotly chart
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

# Verificar si se hizo clic en el botón del gráfico de dispersión
if scatter_button:
    # Mostrar un mensaje indicando la creación del gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión utilizando Plotly Express
    fig = px.scatter(car_data,x="model_year", y="price", color="fuel")
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig, use_container_width=True)