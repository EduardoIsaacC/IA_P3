import heapq

def dijkstra_step_by_step(graph, start):
    """
    graph: diccionario de la forma:
        {
            "A": {"B": 4, "C": 2},
            "B": {"C": 5, "D": 10},
            "C": {"D": 3},
            "D": {}
        }

    start: nodo inicial (ej. "A")
    """
    INF = float("inf")

    # Distancias iniciales: infinito para todos menos el inicio
    dist = {node: INF for node in graph}
    dist[start] = 0

    # Predecesor de cada nodo (para reconstruir caminos)
    prev = {node: None for node in graph}

    # Cola de prioridad (min-heap) -> (distancia_acumulada, nodo)
    pq = [(0, start)]

    # Conjunto de nodos ya visitados (ya se les fijó su distancia mínima)
    visited = set()

    step = 0
    print("=== SIMULACIÓN DEL ALGORITMO DE DIJKSTRA ===")
    print(f"Nodo inicial: {start}\n")

    # Mientras haya nodos por procesar
    while pq:
        step += 1
        print(f"\n--- Paso {step} ---")
        print("Contenido de la cola (distancia, nodo):", pq)

        # Sacar el nodo con menor distancia provisional
        d, u = heapq.heappop(pq)
        print(f"Se extrae el nodo '{u}' con distancia provisional {d}")

        # Si ya fue visitado, lo ignoramos
        if u in visited:
            print(f"El nodo '{u}' ya fue visitado. Se ignora.")
            continue

        # Marcamos u como visitado
        visited.add(u)
        print("Conjunto de nodos visitados ahora:", visited)

        # Relajación de las aristas que salen de u
        for v, w in graph[u].items():
            print(f"  Revisando arista {u} -> {v} con peso {w}")

            if v in visited:
                print(f"    El nodo {v} ya está visitado, se omite.")
                continue

            nueva_dist = dist[u] + w
            print(f"    Distancia actual a {v}: {dist[v]}")
            print(f"    Nueva posible distancia a {v} pasando por {u}: {nueva_dist}")

            # Si encontramos un camino más corto, actualizamos
            if nueva_dist < dist[v]:
                print(f"    ¡Se mejora la distancia a {v}! {dist[v]} -> {nueva_dist}")
                dist[v] = nueva_dist
                prev[v] = u
                heapq.heappush(pq, (nueva_dist, v))
            else:
                print(f"    No se mejora la distancia a {v}")

        print("\nResumen después de este paso:")
        print("  Distancias:", dist)
        print("  Predecesores:", prev)

    print("\n=== FIN DE LA SIMULACIÓN ===")
    print("Distancias finales más cortas desde", start, ":", dist)
    print("Árbol de predecesores:", prev)
    return dist, prev


def reconstruir_camino(prev, start, end):
    """
    Reconstruye el camino más corto desde 'start' hasta 'end'
    usando el diccionario de predecesores 'prev'.
    """
    camino = []
    nodo = end

    # Recorremos hacia atrás desde end hasta start
    while nodo is not None:
        camino.append(nodo)
        nodo = prev[nodo]

    camino.reverse()

    # Si el primer nodo no es el inicio, significa que no hay camino
    if not camino or camino[0] != start:
        return None

    return camino


if __name__ == "__main__":
    # Ejemplo de grafo
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 5, "D": 10},
        "C": {"D": 3},
        "D": {}
    }

    # Nodo inicial
    inicio = "A"

    # Ejecutar simulación paso a paso
    distancias, predecesores = dijkstra_step_by_step(graph, inicio)

    # Ejemplo: reconstruir camino más corto de A a D
    destino = "D"
    camino = reconstruir_camino(predecesores, inicio, destino)
    print(f"\nCamino más corto de {inicio} a {destino}: {camino}")
    print(f"Distancia total: {distancias[destino]}")
