import pandas as pd


# Tarea 3-A
def contar_valor(data, columna, valor):
    """Cuenta el número de registros que tiene un determinado valor
    en una columna.

    Args:
        data: conjuntos de datos (DataFrame).
        columna: columna sobre la que se filtrará (cadena de caracteres).
        valor: valor con el cual se filtrará (cadena de caracteres)

    Returns:
        Número de registros con el valor en la columna.
    """
    return len(data.loc[data[columna] == valor])


# Tarea 3-B
def contar_contenido(data, columna, contenido):
    """Cuenta el número de registros que contienen una sun palabra
    en una determinada columna.

    Args:
        data: conjuntos de datos (DataFrame).
        columna: columna en la que se realizará la búsqueda
                 (cadena de caracteres).
        contenido: palabra que será buscada (cadena de caracteres)

    Returns:
        Número de registros que contienen la palabra en la columna dada.
    """
    return len(data.loc[data[columna].str.contains(contenido, case=False)])


# Tarea 3-C
def contar_decada(data, decada):
    """Cuenta el número de canciones se publicaron en una década.

    Args:
        data: conjuntos de datos (DataFrame).
        década: año inicial desde el que se cuenta la década (valor entero).

    Returns:
        Número de canciones se publicaron en una década
    """
    return len(data.loc[data["release_year"].between(decada, decada+9)])


# Tarea 4-D
def max_popularity(data, anios, anio_actual=2022):
    """Devuelve la canción más popular de los últimos años.

    Args:
        data: conjuntos de datos (DataFrame).
        anios: años en los que se buscará la canción (valor entero).

    Returns:
        Canción más popular de los últimos `anios` años
    """

    idx = (data["popularity"]
           .loc[data["release_year"]
           .between(anio_actual-anios, anio_actual)]
           .idxmax())
    return data["name"].iloc[idx]


# Tarea 4-E
def all_decades(data, inicio, fin=2030):
    """Devuelve la lista de artistas que han publicado canciones en cada una
    de las últimas décadas.

    Args:
        data: conjuntos de datos (DataFrame).
        inicio: año desde el que se buscará que hayan publicado (valor entero).

    Returns:
        Lista de artistas que han publicado canciones en cada una de las
        últimas décadas desde el año `inicio`.
    """
    # Seleccionamos los años en que cada artista ha publicado al menos
    # una canción desde el año `inicio`
    temp = (data[["name_artist", "release_year"]]
            .loc[data["release_year"] >= inicio]
            .drop_duplicates())
    # Agrupamos por década los años
    temp["release_year"] = pd.cut(temp["release_year"],
                                  bins=range(inicio-1, fin, 10))
    # Eliminamos duplicados
    temp = temp.drop_duplicates()
    # Contamos el número de décadas en las que publicó
    temp = temp["name_artist"].value_counts()
    # Devolvemos los que tienen publicados en todas las décadas
    return list(temp[temp == (fin-inicio)//10].index)


if __name__ == "__main__":
    from Tarea1 import lectura_archivo

    # Leemos los datos
    data = lectura_archivo("data/data.zip")
    # Respondemos la pregunta A
    print("La cantidad de canciones de Radiohead es:",
          contar_valor(data, "name_artist", "Radiohead"))
    # Respondemos la pregunta B
    print("La cantidad de canciones que contienen la palabra 'police' es:",
          contar_contenido(data, "name", "police"))
    # Respondemos la pregunta C
    print("La cantidad de álbumes publicados en la década del 1990 es:",
          contar_decada(data, 1990))
    # Respondemos la pregunta D
    print("La canción con más popularidad de los últimos 10 años es:",
          max_popularity(data, 10))
    # Respondemos la pregunta E
    print("Los artistas que tienen canciones en cada una de las",
          "décadas desde el 1960 son:",
          all_decades(data, 1960))
