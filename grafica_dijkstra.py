import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    """
    Igual que antes pero sin tantos prints.
    Devuelve distancias y predecesores.
    """
    INF = float("inf")
    dist = {node: INF for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}

    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u].items():
            if v in visited:
                continue

            nueva_dist = dist[u] + w
            if nueva_dist < dist[v]:
                dist[v] = nueva_dist
                prev[v] = u
                heapq.heappush(pq, (nueva_dist, v))

    return dist, prev


def reconstruir_camino(prev, start, end):
    camino = []
    nodo = end
    while nodo is not None:
        camino.append(nodo)
        nodo = prev[nodo]
    camino.reverse()
    if not camino or camino[0] != start:
        return None
    return camino


def dibujar_grafo_con_camino(graph, path=None):
    """
    graph: diccionario de adyacencia
    path: lista de nodos que forman el camino más corto, ejemplo ["A","C","D"]
    """
    G = nx.DiGraph()  # Dirigido (puedes usar Graph() si es no dirigido)

    # Agregar nodos y aristas con pesos
    for u in graph:
        for v, w in graph[u].items():
            G.add_edge(u, v, weight=w)

    # Posiciones de los nodos (spring_layout = distribución automática)
    pos = nx.circular_layout(G)

    # Dibujar todos los nodos y aristas
    nx.draw(G, pos, with_labels=True, node_size=800)

    # Dibujar etiquetas de pesos en las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Si hay un camino, resaltarlo
    if path is not None and len(path) > 1:
        # Crear una lista de aristas (u,v) que forman el camino
        edges_path = list(zip(path[:-1], path[1:]))

        # Dibujar esas aristas encima, más gruesas
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges_path,
            width=3  # más grueso
        )

    plt.title("Grafo con camino más corto resaltado")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    # Mismo grafo de ejemplo
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 5, "D": 10},
        "C": {"D": 3},
        "D": {}
    }

    inicio = "A"
    destino = "D"

    distancias, predecesores = dijkstra(graph, inicio)
    camino = reconstruir_camino(predecesores, inicio, destino)

    print("Distancias:", distancias)
    print("Predecesores:", predecesores)
    print(f"Camino más corto de {inicio} a {destino}: {camino}")
    print(f"Distancia total: {distancias[destino]}")

    # Dibujar grafo marcando el camino más corto
    dibujar_grafo_con_camino(graph, camino)
