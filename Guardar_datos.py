import os
import pandas as pd

# -----------------------------------------------------------
# Paso 4 - Guardar DataFrames procesados (SOBREESCRIBE SIEMPRE)
# -----------------------------------------------------------

def guardar_datos(datasets_dict):
    """
    Guarda DataFrames en:
    C:/Users/felip/Documents/Portafolio_Jupyter/data/processed

    Sobrescribe siempre los archivos para evitar duplicados.

    Parámetro:
    ----------
    datasets_dict : dict
        Ejemplo:
        {
            "peliculas": df_peliculas,
            "ventas": df_ventas
        }
    """

    # Ruta fija de salida (según tu proyecto)
    base_path = r"C:\Users\felip\Documents\Portafolio_Jupyter\data\processed"

    # Crear la carpeta si no existe
    os.makedirs(base_path, exist_ok=True)

    rutas_finales = {}

    # Guardar cada DataFrame como CSV
    for nombre, df in datasets_dict.items():
        ruta = os.path.join(base_path, f"{nombre}_clean.csv")
        df.to_csv(ruta, index=False)   # <-- esto sobreescribe siempre
        rutas_finales[nombre] = ruta

    return rutas_finales
