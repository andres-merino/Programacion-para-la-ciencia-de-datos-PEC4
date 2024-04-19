import pandas as pd


def get_column_pandas(ruta, columna):
    """Lee una columna del archivo csv utilizando pandas.

    Args:
        ruta: ruta del archivo .csv del que se leerán
              de datos (cadena de caracteres).
        columna: nombre de la columna que será leída
                 (cadena de caracteres)

    Returns:
        Lista de los datos leídos.
    """
    df_pandas = pd.read_csv(ruta, delimiter=';')
    return list(df_pandas[columna])


def get_column_byline(ruta, columna):
    """Lee una columna del archivo csv leyendo el archivo línea a línea.

    Args:
        ruta: ruta del archivo .csv del que se leerán
              de datos (cadena de caracteres).
        columna: nombre de la columna que será leída
                 (cadena de caracteres)

    Returns:
        Lista de los datos leídos.
    """
    # Generamos una lista vacía
    lista = []
    # Abrimos el archivo
    with open(ruta, 'r') as datos:
        # Leemos los encabezados
        encabezados = datos.readline()
        # Seleccionamos el índice al que corresponde la columna que leeremos
        indice = encabezados.split(';').index(columna)
        # Leemos el archivo línea a línea
        for linea in datos:
            # Agregamos los datos a la lista
            lista.append(linea.split(';')[indice])
    # Devolvemos la lista
    return lista


if __name__ == "__main__":
    import timeit
    import matplotlib.pyplot as plt

    # Tomamos las listas de tiempos y número de líneas
    tiempo_pandas = []
    tiempo_byline = []
    lineas = []
    # Tomamos las listas de archivos y columnas que leeremos
    rutas = ["artists_norm.csv", "albums_norm.csv", "tracks_norm.csv"]
    columnas = ["artist_id", "album_id", "track_id"]
    # Evaluamos la función para cada archivo
    for ruta, columna in zip(rutas, columnas):
        # Medimos el tiempo con la funcion de pandas
        temp = []
        inicio = timeit.default_timer()
        temp = get_column_pandas(ruta, columna)
        fin = timeit.default_timer()
        tiempo_pandas.append(fin-inicio)
        # Medimos el tiempo con la función por líneas
        temp = []
        inicio = timeit.default_timer()
        temp = get_column_byline(ruta, columna)
        fin = timeit.default_timer()
        tiempo_byline.append(fin-inicio)
        # Medimos el número de líneas
        lineas.append(len(temp))
    # Generamos el gráfico
    plt.plot(lineas, tiempo_pandas, '-')
    plt.plot(lineas, tiempo_byline, '-')
    plt.xlabel("No. líneas")
    plt.ylabel("Tiempo")
    plt.title("No. líneas vs Tiempo")
    plt.legend(["pandas", "byline"])
    plt.show()
