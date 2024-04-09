from data_reader import leer_datos, filtrar_calcular_media
import pandas as pd

def main():
    ruta_archivo = "data\datos_examen.csv"

    nombre = "Miguel"
    
    df = leer_datos(ruta_archivo)

    df_filtered =  filtrar_calcular_media(df, nombre)


if __name__ == "__main__":
    main()