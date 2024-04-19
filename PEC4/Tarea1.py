import zipfile as zf
import pandas as pd


def lectura_archivo(archivo):
    """Lee los archivos con los datos genera el conjunto de datos que se
    utilizará en el proyecto.

    Args:
        archivo: ruta del archivo .zip donde están los archivos
                 de datos (cadena de caracteres).

    Returns:
        Conjunto de datos en formato DataFrame de pandas.
    """
    # Descomprimimos el archivo .zip
    with zf.ZipFile(archivo, 'r') as zip_f:
        zip_f.extractall()
    # Leemos los tres archivos csv
    df_albums = pd.read_csv("albums_norm.csv", delimiter=';')
    df_artists = pd.read_csv("artists_norm.csv", delimiter=';')
    df_tracks = pd.read_csv("tracks_norm.csv", delimiter=';')
    # Agregamos la información de artistas a las canciones
    df_temp = df_tracks.merge(df_artists, on='artist_id',
                              how="left", suffixes=('', "_artist"))
    # Agregamos la información de los álbumes a las canciones
    df_final = df_temp.merge(df_albums, on=['album_id', 'artist_id'],
                             how="left", suffixes=('', "_album"))
    # Corregimos los nombre de los artistas para que inicie cada
    # palabra en mayúscula.
    df_final["name_artist"] = df_final["name_artist"].str.title()
    # Imputamos los datos faltantes en popularidad con el promedio
    promedio = df_final["popularity"].mean()
    df_final["popularity"] = df_final["popularity"].fillna(promedio)
    # Devolvemos el conjunto de datos
    return df_final


if __name__ == "__main__":
    import os
    # Generamos la lectura de los archivos
    data = lectura_archivo(os.path.join("data", "data.zip"))
    # Mostramos en pantalla los criterios solicitados
    print("El número de canciones es:", data.shape[0])
    print("El número de columnas es:", data.shape[1])
    df_tracks = pd.read_csv("tracks_norm.csv", delimiter=';')
    print("El numero de canciones que no tienen valor de popularidad es:",
          df_tracks["popularity"].isnull().sum())
