import matplotlib.pyplot as plt


def histograma(data, artista, columna, **kwargs):
    """Devuelve el histograma de un artista correspondiente a una feature.

    Args:
        data: conjuntos de datos (DataFrame).
        artista: nombre del artista (cadena de caracteres).
        columna: feature que se tomará para el histograma
                 (cadena de carcteres).
        **kwargs: opciones enviadas al gráfico.

    Returns:
        Histograma de un artista correspondiente a una feature.
    """
    # Seleccionamos los datos que se utilizarán
    temp = data[columna].loc[data["name_artist"] == artista]
    # Generamos el gráfico
    graf = temp.plot.hist(density=True, **kwargs,
                          title=artista+" - "+columna) \
               .set(xlabel=columna, ylabel="Densidad")
    return graf


if __name__ == "__main__":
    from Tarea1 import lectura_archivo

    # Tomamos las listas de tiempos y número de líneas
    data = lectura_archivo("data/data.zip")
    # Generamos el gráfico y lo mostramos
    histograma(data, "Ed Sheeran", "acousticness", color="skyblue")
    plt.show()
