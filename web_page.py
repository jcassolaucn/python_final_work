# @copyright: 2024/07/23
# @author: Ing. Jose Manuel Cassola Bacallao
# @version: 1.0
# @license: Apache 2.0

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title='Análisis de Datos Meteorológicos', layout='wide')

# Título
st.title('Análisis de Datos Meteorológicos')


# Cargar los datos
@st.cache_data
def load_data():
    file_path = 'data/data.csv'
    data = pd.read_csv(file_path, delimiter=';', na_values=['.'])
    data['fecha'] = pd.to_datetime(data['fecha'], format='%y%m%d', errors='coerce')
    data['fecha_temperatura_minima'] = pd.to_datetime(data['fecha_temperatura_minima'], format='%y%m%d',
                                                      errors='coerce')
    data['fecha_temperatura_maxima'] = pd.to_datetime(data['fecha_temperatura_maxima'], format='%y%m%d',
                                                      errors='coerce')
    data.fillna(data.mean(), inplace=True)
    return data


data = load_data()

# Mostrar los datos
if st.checkbox('Mostrar datos crudos'):
    st.write(data)

# Filtros interactivos
st.sidebar.header('Filtros')
start_date = st.sidebar.date_input('Fecha de inicio', data['fecha'].min())
end_date = st.sidebar.date_input('Fecha de fin', data['fecha'].max())

if start_date > end_date:
    st.sidebar.error('La fecha de inicio no puede ser posterior a la fecha de fin.')

filtered_data = data[(data['fecha'] >= pd.to_datetime(start_date)) & (data['fecha'] <= pd.to_datetime(end_date))]

# Visualizaciones
st.header('Visualizaciones')

# Heatmap de correlación
st.subheader('Heatmap de Correlación')
corr = filtered_data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Pairplot
st.subheader('Pairplot')
fig2 = sns.pairplot(filtered_data[['so2_validado', 'mp_2_5_validado', 'mp_10_validado', 'temperatura_media']])
st.pyplot(fig2)

# Gráfico de dispersión interactivo
st.subheader('Gráfico de Dispersión Interactivo')
x_axis = st.selectbox('Seleccione el eje X', options=filtered_data.columns)
y_axis = st.selectbox('Seleccione el eje Y', options=filtered_data.columns)
scatter_fig = px.scatter(filtered_data, x=x_axis, y=y_axis, title=f'{y_axis} vs {x_axis}')
st.plotly_chart(scatter_fig)

# Gráfico de líneas de tiempo interactivo
st.subheader('Líneas de Tiempo Interactivas')
line_fig = px.line(filtered_data, x='fecha', y=['so2_validado', 'mp_2_5_validado', 'mp_10_validado'],
                   title='Tendencias en el Tiempo')
st.plotly_chart(line_fig)
