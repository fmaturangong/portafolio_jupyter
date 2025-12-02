import os
import pandas as pd

# Directorio base (fijo)
BASE_PATH = r"C:/Users/felip/Documents/Portafolio_Jupyter"

# AHORA RAW_PATH APUNTA AL LUGAR REAL DONDE ESTÁN LOS ARCHIVOS
RAW_PATH = BASE_PATH

# Subcarpetas opcionales si las necesitas más adelante
PROCESSED_PATH = os.path.join(BASE_PATH, "data", "processed")
CLEAN_PATH = os.path.join(BASE_PATH, "data", "clean")

# Crear carpetas (solo processed y clean)
os.makedirs(PROCESSED_PATH, exist_ok=True)
os.makedirs(CLEAN_PATH, exist_ok=True)

# Rutas de archivos RAW
rutaPeliculas = os.path.join(RAW_PATH, "Top-Películas.csv")
rutaVentas = os.path.join(RAW_PATH, "Ventas.csv")
rutaPeliculas200 = os.path.join(RAW_PATH, "peliculas_100_2005_2024.xlsx")

# Funciones de carga
def load_raw_peliculas(path=rutaPeliculas):
    print("Cargando:", path)
    return pd.read_csv(path)

def load_raw_ventas(path=rutaVentas):
    print("Cargando:", path)
    return pd.read_csv(path)

def load_raw_peliculas_200(path=rutaPeliculas200):
    print("Cargando:", path)
    return pd.read_excel(path)
