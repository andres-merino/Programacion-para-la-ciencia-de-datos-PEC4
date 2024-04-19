import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def call_info(nombre_artista):

    url = "https://www.theaudiodb.com/api/v1/json/2/search.php?s="
    response = requests.get(url+nombre_artista)
    if response.json()["artists"] is None:
        artist_fm_y = ""
        artist_country = ""
    else:
        artist_fm_y = response.json()["artists"][0]["intFormedYear"]
        artist_country = response.json()["artists"][0]["strCountry"]

    return nombre_artista, artist_fm_y, artist_country


def call_info_list(lista_nombres):
    # Inicializamos las listas
    futures = []
    resultados = []
    with ThreadPoolExecutor() as executor:
        for nombre in lista_nombres:
            futures.append(executor.submit(call_info, nombre))
        # Guardamos los resultados
        for future in as_completed(futures):
            resultados.append(future.result())

    info = pd.DataFrame(resultados, columns=["artist_name", "formed_year",
                                             "country"])
    return info


if __name__ == "__main__":
    from Tarea2 import *

    print(call_info("Radiohead"))
    print(call_info("David Bowie"))
    print(call_info("Måneskin"))

    lista = get_column_byline("artists_norm.csv", "name")
    try:
        data = call_info_list(lista[:40])
        data.to_csv("datos_descargados.csv")
        print("Los datos se encuentran en el archivo datos_descargados.csv",
        	  "\nSe descargaron 40 registros para no saturar la API")
    except:
        print("Ocurrió un error, posiblemente se saturó la API.")
