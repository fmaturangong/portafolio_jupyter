Análisis de Películas, Ventas y Rentabilidad Financiera

Proyecto de análisis de datos desarrollado en Jupyter Notebook enfocado en el estudio de películas y ventas comerciales. Integra procesos de carga, limpieza, transformación y visualización de datos, junto con modelos predictivos para evaluar desempeño financiero y rentabilidad.

a) Objetivo del Proyecto

Analizar información de películas y ventas para comprender el comportamiento financiero y comercial, con el fin de:

Identificar géneros y años con mayor recaudación.

Analizar la distribución de ventas por categoría de producto.

Explorar patrones y relaciones entre variables.

Evaluar la relación entre costos de producción y recaudación.

Estimar la probabilidad de que una película sea rentable.

b) Archivos Incluidos

Carga_datos.py – Carga de archivos CSV y Excel desde el sistema local.

Limpieza_datos.py – Depuración, eliminación de nulos y duplicados.

transformar_datos.py – Normalización de columnas y valores categóricos.

guardar_datos.py – Persistencia de datasets procesados.

Graficos_carga.py – Generación de gráficos y análisis visual.

main.ipynb – Notebook principal que ejecuta el flujo completo del proyecto.

c) Análisis Realizados

Recaudación de Películas por Género y Año
Permite identificar qué géneros y periodos presentan mejor desempeño en taquilla mediante gráficos de líneas y barras.

Distribución de Ventas por Producto
Analiza el peso relativo de cada categoría utilizando gráficos de torta y barras.

Distribución y Variabilidad de Ventas
Explora patrones de compra mediante histogramas, KDE y gráficos violin para detectar dispersión y concentración.

Relaciones entre Variables de Venta
Utiliza PairGrid y Pairplot para identificar correlaciones y comportamientos multivariados.

Regresión Lineal: Costos vs. Recaudación
Evalúa la relación entre inversión y retorno económico en películas, identificando tendencias generales.

Regresión Logística: Probabilidad de Rentabilidad
Clasifica películas como rentables o no rentables y estima la probabilidad de éxito financiero según los costos.

d) Tecnologías Utilizadas

Python

Jupyter Notebook

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn
