import pandas as pd
import matplotlib.pyplot as plt


def histograma_comp(data, artista1, artista2, columna, **kwargs):
    """Devuelve los histograma de dos artistas correspondiente a una feature
    para comparación.

    Args:
        data: conjuntos de datos (DataFrame).
        artista1: nombre del primer artista (cadena de caracteres).
        artista2: nombre del segundo artista (cadena de caracteres).
        columna: feature que se tomará para el histograma
                 (cadena de carcteres).
        **kwargs: opciones enviadas al gráfico.

    Returns:
        Histogramas de dos artistas correspondiente a una feature
        para comparación.
    """
    # Seleccionamos los datos que se utilizarán
    temp = pd.DataFrame({artista1: (data[columna]
                                    .loc[data["name_artist"] == artista1]),
                         artista2: (data[columna]
                                    .loc[data["name_artist"] == artista2])})
    # Generamos el gráfico
    graf = temp.plot.hist(density=True, alpha=0.5,
                          bins=[i/10 for i in range(11)], **kwargs)\
               .set(xlabel="energy", ylabel="Densidad",
                    title=columna+": "+artista1+" vs "+artista2)
    return graf


if __name__ == "__main__":
    from Tarea1 import lectura_archivo

    # Tomamos las listas de tiempos y número de líneas
    data = lectura_archivo("data/data.zip")
    # Generamos el gráfico y lo mostramos
    histograma_comp(data, "Adele", "Extremoduro", "energy")
    plt.show()
