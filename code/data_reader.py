import pandas as pd

def leer_datos (ruta_archivo: str) -> pd.DataFrame:
    """ 
    Paso uno del ejercicio, leer el csv 
    y pasar el TS a datetime de todo el dateframe
    """
    
    df = pd.read_csv(ruta_archivo)
    df["TS"] = pd.to_datetime(df["TS"])
    return df


def filtrar_calcular_media(df: pd.DataFrame, nombre: str) -> pd.DataFrame:
    """ 
    Filtar y calcular la media para alumno Miguel
    """

    df_filtered = df[df["Tag"] == "Examen_" + nombre] 
    media = df_filtered["Value"].mean()
    print(f"La media de Valores para la Tag {nombre} es: ", media)
    
    return df_filtered