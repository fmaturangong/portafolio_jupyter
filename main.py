import pandas as pd

# Importar módulos del pipeline
from Carga_datos import load_raw_peliculas, load_raw_ventas, load_raw_peliculas_200
from Limpieza_datos import clean_peliculas, clean_ventas
from transformar_datos import transformar_datos
from guardar_datos import guardar_datos
from graficos_carga import (
    crear_grafico_peliculas_mayor_recaudacion,
    distribucion_categoria_productos
)

# ---------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------
def main():

    print("📥 1) Cargando datos RAW...")
    df_peliculas_raw = load_raw_peliculas()
    df_ventas_raw = load_raw_ventas()
    df_peliculas200_raw = load_raw_peliculas_200()

    print("🧹 2) Limpiando datos...")
    df_peliculas_clean = clean_peliculas()
    df_ventas_clean = clean_ventas()

    print("🔧 3) Transformando datos...")
    df_peliculas_trans = transformar_datos(df_peliculas_clean)
    df_ventas_trans = transformar_datos(df_ventas_clean)
    df_peliculas200_trans = transformar_datos(df_peliculas200_raw)

    print("💾 4) Guardando datasets procesados...")
    rutas = guardar_datos({
        "peliculas": df_peliculas_trans,
        "ventas": df_ventas_trans,
        "peliculas_200": df_peliculas200_trans
    })

    print("📊 5) Generando gráficos...")
    crear_grafico_peliculas_mayor_recaudacion(df_peliculas_trans)
    distribucion_categoria_productos(df_ventas_trans)

    print("✔️ Pipeline completado.")
    print("📁 Archivos guardados en:")
    for nombre, ruta in rutas.items():
        print(f"   - {nombre}: {ruta}")


if __name__ == "__main__":
    main()

from main import main
main()
