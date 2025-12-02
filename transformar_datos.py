import pandas as pd
import numpy as np

def transformar_datos(df):
    df = df.copy()

    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.normalize("NFKD")
        .str.encode("ascii", "ignore")
        .str.decode("utf-8")
    )

    # Normalizar SOLO strings
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.lower()
            .str.normalize("NFKD")
            .str.encode("ascii", "ignore")
            .str.decode("utf-8")
        )

    # Columna de faltantes
    df["faltantes"] = df.isna().sum(axis=1)

    return df
