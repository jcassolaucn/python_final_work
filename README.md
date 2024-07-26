# Análisis de Datos Meteorológicos

## Descripción del Proyecto

Este proyecto consiste en el análisis de datos meteorológicos y de calidad del aire provenientes de una estación
meteorológica. Utiliza Python para la carga y procesamiento de datos, el análisis exploratorio de datos (EDA), y la
construcción de modelos predictivos. Además, incluye una aplicación web interactiva desarrollada con Streamlit que
permite a los usuarios explorar los datos y visualizaciones de forma intuitiva.

## Estructura del Proyecto

```
project/
│
├── data/
│   └── data.csv # Archivo CSV con los datos meteorológicos
│
├── notebooks/
│   └── air_quality.ipynb # Notebook Jupyter para análisis de datos y EDA
│
├── web_page.py # Aplicación web Streamlit
│
├── environment.yml # Archivo de configuración para el entorno virtual
│
├── requirements.txt # Archivo de requerimientos para el entorno virtual
│
└── README.md # Descripción del proyecto
```

## Instalación y Ejecución

### Prerrequisitos

- Python 3.x
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

### Ejecución de la Aplicación Web

Para ejecutar la aplicación web con Streamlit, navega al directorio app y ejecuta:

```bash
streamlit run web_page.py
```

Esto abrirá la aplicación en tu navegador predeterminado.

### Descripción de los Archivos
<ul>
    <li>data.csv: Contiene los datos meteorológicos con las siguientes columnas:</li>
        <ul>
          <li>fecha</li>
          <li>so2_validado</li>
            <li>so2_preliminar</li>
            <li>so2_no_validado</li>
            <li>temperatura_media</li>
            <li>fecha_temperatura_minima</li>
            <li>temperatura_minima</li>
            <li>fecha_temperatura_maxima</li>
            <li>temperatura_maxima</li>
            <li>mp_2_5_validado</li>
            <li>mp_2_5_no_validado</li>
            <li>mp_10_validado</li>
            <li>mp_10_no_validado</li>
        </ul>
      <li>air_quality.ipynb: Notebook Jupyter que contiene el análisis exploratorio de datos (EDA) y la construcción del modelo predictivo.</li>
      <li>web_page.py: Script de la aplicación web Streamlit que permite a los usuarios interactuar con los datos y visualizar los resultados del análisis.</li>
</ul>

## Análisis Exploratorio de Datos (EDA)
El análisis exploratorio de datos incluye:
<ul>
    <li>Estadísticas descriptivas de las variables.</li>
    <li>Visualización de la distribución de las variables utilizando Seaborn y Matplotlib.</li>
    <li>Identificación y visualización de correlaciones entre variables.</li>
    <li>Creación de visualizaciones avanzadas como heatmaps y pairplots.</li>
</ul>

## Construcción de Modelos Predictivos
Se construyó un modelo de regresión lineal para predecir los valores de SO2, MP2.5 y MP10 a partir de la fecha y la
temperatura media. Las métricas de evaluación del modelo incluyen:
<ul>
    <li>Mean Squared Error (MSE):</li>
    <li>Mean Absolute Error (MAE):</li>
    <li>R-squared (R2):</li>
</ul>

## Aplicación Web con Streamlit
La aplicación web incluye las siguientes funcionalidades:
<ul>
    <li>Visualización de los datos crudos.</li>
    <li>Filtros interactivos para seleccionar rangos de fechas.</li>
    <li>Visualización de correlaciones entre variables con heatmaps.</li>
    <li>Visualización de relaciones entre variables con pairplots y gráficos de dispersión interactivos.</li>
    <li>Visualización de tendencias temporales con gráficos de líneas de tiempo interactivos.</li>
</ul>

## Futuras Mejoras
<ul>
    <li>Agregar más características: Incluir otras variables relevantes como humedad y velocidad del viento.</li>
    <li>Ingeniería de características: Generar nuevas características a partir de las existentes.</li>
    <li>Modelos más complejos: Probar modelos avanzados como Random Forest, Gradient Boosting o redes neuronales.</li>
    <li>Tuning de hiperparámetros: Ajustar los hiperparámetros del modelo utilizando técnicas como Grid Search o Random Search.</li>
    <li>Validación cruzada: Utilizar validación cruzada para evitar sobreajuste y obtener mejores estimaciones del desempeño del modelo.</li>
</ul>

## Contacto
Para cualquier consulta o sugerencia, puedes contactarme a través de jose.cassola@alumnos.ucn.cl.