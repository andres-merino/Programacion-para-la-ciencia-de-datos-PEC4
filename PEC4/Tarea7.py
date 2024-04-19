from numpy import dot
from numpy.linalg import norm
import seaborn as sns
import matplotlib.pylab as plt


def dist_cousinus(x, y):
    """Devuelve la distancia de similitud de coseno.

    Args:
        x, y: lista de datos (lista)

    Returns:
        Distancia de similitud de coseno.
    """
    return dot(x, y)/(norm(x)*norm(y))


def dist_euclidea(x, y):
    """Devuelve la distancia euclidea.

    Args:
        x, y: lista de datos (lista)

    Returns:
        Distancia de euclidea.
    """
    return norm([i-j for i, j in zip(x, y)])


def matriz_distancias(data, artistas, distancia=dist_euclidea):
    """Devuelve la matriz de distancias entre una lista de artistas.

    Args:
        data: conjuntos de datos (DataFrame).
        artistas: lista de los nombres de los artistas (lista)
        distancia: función de distancia a utilizarse (función). por defecto
                   usa `dist_euclidea`

    Returns:
        Matriz de distancias entre una lista de artistas.
    """
    # Seleccionamos el conjunto de datos
    temp = data[["name_artist", "danceability", "energy", "key",
                 "loudness", "mode", "speechiness", "acousticness",
                 "instrumentalness", "liveness", "valence", "tempo",
                 "time_signature"]]
    # Agrupamos por promedios
    temp = temp.groupby(["name_artist"]).mean()
    # Definimos el tamaño de la matriz
    n = len(artistas)
    # Inicializamos la matriz en 0
    dist_mtrix = [[0 for x in range(n)] for x in range(n)]
    # Llenamos la matriz con el cálculo de las distancias
    for i in range(n):
        for j in range(n):
            art1 = artistas[i]
            art2 = artistas[j]
            dist_mtrix[i][j] = distancia(temp.loc[art1].values,
                                         temp.loc[art2].values)
    # Generamos el gráfico de calor de la matriz
    ax = sns.heatmap(dist_mtrix, linewidth=0.3, cmap="Blues",
                     xticklabels=artistas, yticklabels=artistas,
                     annot=True, fmt='.5g')
    plt.yticks(rotation=0)
    plt.title("Distancias con "+distancia.__name__)
    # Devolvemos la matriz de distancias
    return dist_mtrix, ax


if __name__ == "__main__":
    from Tarea1 import lectura_archivo

    # Leemos los datos
    data = lectura_archivo("data/data.zip")
    # Seleccionamos la lista de artistas
    artistas = ["Metallica", "Extremoduro", "Ac/Dc", "Hans Zimmer"]
    # Generamos el histograma con cada distancia
    matriz_distancias(data, artistas, dist_euclidea)
    plt.show()
    matriz_distancias(data, artistas, dist_cousinus)
    plt.show()
