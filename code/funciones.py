import pandas as pd

def leer_datos (ruta_csv):
    """ Paso uno del ejercicio, leer el csv 
    y pasar el TS a datetime de todo el dateframe"""
    
    df = pd.read_csv("..\data\datos_examen.csv")
    df["TS"] = pd.to_datetime(df["TS"])
    return df


def filtrar_calcular_media():
     """ Filtar y calcular la media para alumno Miguel"""
#    df_filtered = df[df['Tag']=='Examen_Miguel']
#    df_filtered = 

