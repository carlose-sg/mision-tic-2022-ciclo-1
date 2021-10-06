# ******************************
# Carlos Eduardo Sanchez Guevara
# Grupo 69
# Analisis Reto 5
# Jun 18, 2021
# ******************************
# reto_sem_05_carlose_sanchezg.py

# Importamos la libreria pandas
import pandas as pd

# Importamos la libreria matplotlib
# import matplotlib.pyplot as plt

# Definimos la funcion para lectura del archivo
def infoIcfes(rt_archivo : str) -> dict:

    # Validamos que la extension del archivo sea csv
    extArchivo = rt_archivo.split('.')[-1]
    if extArchivo != 'csv':
        return 'Extensión inválida.'

    try:
        # Generamos el DataFrame a partir de la lectura del archivo
        df = pd.read_csv(rt_archivo, encoding = 'latin-1', engine = 'python')
    except:
        # Sino se puede leer el archivo se retorna un mensaje de error
        return 'Error al leer el archivo de datos.'

    # Identificamos los nombres de las columnas para filtrar los datos
    # print(df)
    # for columna in df.columns:
        # print(columna)

    # Seleccionamos estudiantes con una puntuacion en la prueba de ingles mayor o igual a 60 y menor o igual a 100
    df_filtrar = df.query('punt_ingles >= 60 and punt_ingles <= 100')
    # print(df_filtrar)

    # Filtramos los datos por ocupacion del padre
    df_ocupacion_padre = df_filtrar[['punt_ingles', 'ocupacion_del_padre']]
    # print(df_ocupacion_padre)

    # Se calculan el promedio, la mediana y el total de la puntuacion
    d_promedio = df_ocupacion_padre.groupby("ocupacion_del_padre", as_index = False).mean()
    # print(d_promedio)
    d_mediana = df_ocupacion_padre.groupby("ocupacion_del_padre", as_index = False).median()
    # print(d_mediana)
    d_totales = df_ocupacion_padre.groupby("ocupacion_del_padre", as_index = False).count()
    # print(d_totales)

    # Se combinan los datos en el dataframe
    d_datos = pd.merge(d_promedio, d_mediana, on = "ocupacion_del_padre")
    d_datos = pd.merge(d_datos, d_totales, on = "ocupacion_del_padre")
    
    # Se asignan nombres de columnas
    # La ultima columna lleva el nombre 'Puntación'
    d_datos.columns = ['Ocupacion Padre', 'Promedio', 'Mediana', 'Puntación']

    # Hacemos la impresion del dataframe
    # print(d_datos)

    # Se retorna el dataframe convertido en diccionario
    return d_datos.to_dict()


# Se define la ruta del archivo a leer
# ruta = r'd:\Datos\carlosesg\OneDrive\MISION TIC 2022\01 - CICLO 01\Fundamentos de Programación\Unidad 05\Reto de la Semana\Pruebas_SABER_11_220_estudiantes_2020_1.csv'
ruta = r'https://raw.githubusercontent.com/IsraelArbona/Mision-TIC-GRUPO-09/master/Pruebas_SABER_11_220_estudiantes_2020_1.csv'

# Llamamos la funcion
print(infoIcfes(ruta))
