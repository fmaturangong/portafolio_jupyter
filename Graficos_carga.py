import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# -----------------------------------------------------------


def peliculas_mayor_recaudacion(Peliculas): 
    def Eleccion_genero_anio():
        try: 
            Genero = Peliculas_csv['genero'].unique()
            anio = Peliculas_csv['ano'].unique()
            print("Categorías:", ", ".join(Genero))
            print("**********************************")
            print("Elegir Categoria: ")

            genero_elegido = "animacion"
            print("Elegir Año: ")
            anio_elegido = 2010

            if genero_elegido in Genero and anio_elegido in anio:
                return genero_elegido, anio_elegido
            else:
                print("Genero o año no validos")
                return None, None

        except Exception as e:
            print(f"Error inesperado en Eleccion_genero_anio: {e}")
            return None, None
    

    def crear_grafico_peliculas_mayor_recaudacion(Peliculas):
        Genero_elegido, Anio_elegido = Eleccion_genero_anio()

        # si falló la selección, salimos
        if Genero_elegido is None or Anio_elegido is None:
            print("No se puede crear el gráfico. Género o año inválidos.")
            return

        try: 
            Numero_Peliculas = 10
            Peliculas_Filtrado_Genero_Anio = Peliculas[
                (Peliculas['genero'] == Genero_elegido) &
                (Peliculas['ano'] == Anio_elegido)
            ].head(Numero_Peliculas)

            if Peliculas_Filtrado_Genero_Anio.empty:
                print("No hay películas para ese género y año.")
                return

            sns.relplot(
                data=Peliculas_Filtrado_Genero_Anio,
                y='recaudacion(m)',
                x='titulo',
                kind="line",
                height=5,
                aspect=2
            )

            plt.xticks(rotation=90)
            plt.show()

            sns.catplot(
                data=Peliculas_Filtrado_Genero_Anio,
                y='recaudacion(m)',
                x='titulo',
                kind="bar",
                height=5,
                aspect=2
            )

            plt.xticks(rotation=90)
            plt.show()

        except KeyError as e:
            print(f"Error: Falta una columna en los datos: {e}")

        except Exception as e:
            print(f"Error inesperado en crear_grafico_peliculas_mayor_recaudacion: {e}")


    crear_grafico_peliculas_mayor_recaudacion(Peliculas_csv)

    

####################################################################

#Creacion de grafico que muestra distribucion de categorias para venta de productos

#Datos_Tabla_Ventas = pd.read_csv(rutaVentas)
#cleaner = DataCleaner(Datos_Tabla_Ventas)
#cleaner.drop_na()
#Datos_Tabla_Ventas = cleaner.df

def graficoPie_Ventas_Total_Productos(Ventas):
    Ventas_csv = Ventas.copy()
    print(Ventas_csv.columns)
    print(Ventas_csv.head())
    try:
        Datos_agrupados = Ventas_csv.groupby("producto")['total_venta'].sum()
        Datos_agrupados_DF = pd.DataFrame(Datos_agrupados)
        
        plt.figure(figsize=(8, 6))
        plt.pie(
            Datos_agrupados_DF['total_venta'],
            labels=Datos_agrupados_DF.index,
            autopct='%1.1f%%'
        )
        plt.title("Gráfico de Porcentaje Total de Ventas por Categoría", fontsize=14, fontweight='bold')
        plt.show()

    except KeyError as e:
        print(f"Error: Falta una columna en los datos: {e}")
    except Exception as e:
        print(f"Error inesperado en graficoPie_Ventas_Total_Productos: {e}")


def graficoHist_Distribucion_Productos(Ventas):
    try:
        plt.figure(figsize=(8, 5))
        sns.displot(Ventas, x='producto', kde=True)
        plt.title("Gráfico de Distribución de Productos", fontsize=14, fontweight='bold')
        plt.show()
        
        sns.displot(Ventas, x='total_venta', kind='kde')
        plt.title("Gráfico de flujo de Ventas", fontsize=14, fontweight='bold')
        plt.show()

    except KeyError as e:
        print(f"Error: Falta una columna en los datos: {e}")
    except Exception as e:
        print(f"Error inesperado en graficoHist_Distribucion_Productos: {e}")


def graficobox_Distribucion_Productos(Ventas):
    try:
        sns.catplot(
            data=Ventas,
            y='total_venta',
            x='producto',
            kind="violin",
            height=5,
            aspect=1.5
        )
        plt.title("Distribución de Ventas por Producto Formato Violin", fontsize=14, fontweight='bold')
        plt.show()

        sns.catplot(
            data=Ventas,
            y='total_venta',
            x='producto',
            kind="bar",
            order=['electronic', 'juguetes', 'alimentos', 'ropa', 'libros'], 
            hue = "producto")
        plt.title("Distribución de Ventas por Producto Formato Bar", fontsize=14, fontweight='bold')
        plt.show()

    except KeyError as e:
        print(f"Error: Falta una columna en los datos: {e}")
    except Exception as e:
        print(f"Error inesperado en graficobox_Distribucion_Productos: {e}")


def Relaciones_Pair_Grafico(Ventas):
    try:
        graf_Pair = sns.PairGrid(Ventas, hue="producto", corner=True)
        plt.title("Distribución PairGrid ", fontsize=14, fontweight='bold')
        graf_Pair.map_lower(sns.scatterplot)
        graf_Pair.map_diag(sns.histplot)
        graf_Pair.add_legend()
        plt.show()
        
        plt.title("Distribución PairPlot ", fontsize=14, fontweight='bold')
        graf_pair = sns.pairplot(data = Ventas, hue="producto")
        plt.show()
    except KeyError as e:
        print(f"Error: Falta una columna en los datos: {e}")
    except Exception as e:
        print(f"Error inesperado en PairGrid: {e}")

def RegresionLinear(Peliculas_200):
    print(Peliculas_200.columns.tolist())
    try: 
        plt.scatter(Peliculas_200['Recaudacion_USD'],Peliculas_200['Costos_USD'])
        X = Peliculas_200[['Recaudacion_USD']] 
        Y = Peliculas_200[['Costos_USD']] 
        modelo = linear_model.LinearRegression()
        modelo.fit(X,Y)
        prediccion = modelo.predict(X)
        plt.plot(Peliculas_200['Recaudacion_USD'], prediccion, color='red', label='Regresión lineal')
        plt.xlabel("Recaudación (USD)")   # Título del eje X
        plt.ylabel("Costos (USD)")        # Título del eje Y
        plt.title("Relación entre Recaudación y Costos de Películas")  # Título general
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error al generar la Regresión Lineal: {e}")


def RegresionLogistica(Peliculas_200):
    
    try:
        Peliculas_200['Rentable'] = (Peliculas_200['Recaudacion_USD'] > Peliculas_200['Costos_USD']).astype(int)
        print(Peliculas_200['Rentable'].value_counts())
        # Variables predictoras y objetivo
        X = Peliculas_200[['Costos_USD']]
        Y = Peliculas_200['Rentable']
        
        # División de datos
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.9, random_state=42)
        
        # Modelo de regresión logística
        modelo = LogisticRegression()
        modelo.fit(X_train, Y_train)
        
        # Precisión del modelo
        print("Precisión del modelo:", modelo.score(X_test, Y_test))
        
        # DataFrame de práctica
        Costos = pd.DataFrame({'Costos_USD': [12000000, 22000000, 9000000, 28000000, 1800000, 900000, 30000000, 1400000, 34500000, 12000, 90000, 3432000]})
        
        # Probabilidades de ser rentable
        probabilidades = modelo.predict_proba(Costos)
        prob = probabilidades[:, 1]  # columna de probabilidad de Rentable = 1
        
        # --- Gráficos ---
        plt.figure(figsize=(8,6))
        plt.scatter(Peliculas_200['Costos_USD'], Peliculas_200['Rentable'], color='red', label='Datos reales')
        plt.scatter(Costos['Costos_USD'], prob, color='blue', label='Probabilidad predicha')
        
        plt.xlabel("Costos (USD)")
        plt.ylabel("Probabilidad de ser rentable")
        plt.title("Probabilidad de rentabilidad según los costos")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error al generar la Regresión Logistica: {e}")

def distribucion_categoria_productos(Peliculas, Ventas, Peliculas_200):
    try:
        #peliculas_mayor_recaudacion(Peliculas)
        #graficoPie_Ventas_Total_Productos(Ventas)
        #graficoHist_Distribucion_Productos(Ventas)
        #graficobox_Distribucion_Productos(Ventas)
        #Relaciones_Pair_Grafico(Ventas)
        RegresionLinear(Peliculas_200)
        RegresionLogistica(Peliculas_200)
    except Exception as e:
        print(f"Error al generar los gráficos de distribución: {e}")

