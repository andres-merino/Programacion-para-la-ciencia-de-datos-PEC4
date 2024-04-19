import pandas as pd
import matplotlib.pyplot as plt


# Tarea 4-A
def max_min_mean_energy(data, artist):
    """Calcula las estadísticas básicas de la columna energy de un artista.

    Args:
        data: conjuntos de datos (DataFrame).
        artist: nombre del artista (cadena de caracteres)

    Returns:
        Máximo, mínimo y promedio de la columna energy de un artista.
    """
    temp = data["energy"].loc[data["name_artist"] == artist]
    return [temp.max(), temp.min(), temp.mean()]


# Tarea 4-B
def mean_by_album(data, artist, column="danceability"):
    """Calcula la media de un feature de un artista, agrupado por álbumes.

    Args:
        data: conjuntos de datos (DataFrame).
        artist: nombre del artista (cadena de caracteres)
        column: nombre de la columna (cadena de caracteres),
                valor por defecto "danceability"

    Returns:
        Máximo, mínimo y promedio de la columna energy de un artista.
    """
    # Seleccionamos los datos por promedios
    means = (data[["name_album", column]]
             .loc[data["name_artist"] == artist]
             .groupby(["name_album"]).mean())
    # Generamos el gráfico
    means.plot(kind="bar")
    plt.show()
    return means


if __name__ == "__main__":
    from Tarea1 import lectura_archivo

    # Tomamos las listas de tiempos y número de líneas
    data = lectura_archivo("data/data.zip")
    # Mostramos las estadísticas básicas de A
    estadisticas = max_min_mean_energy(data, "Metallica")
    print("El máximo de energy de todas las canciones de Metallica es:",
          estadisticas[0])
    print("El mínimo de energy de todas las canciones de Metallica es:",
          estadisticas[1])
    print("La media de energy de todas las canciones de Metallica es:",
          estadisticas[2])
    # Mostramos la gráfica de B
    mean_by_album(data, "Coldplay")
