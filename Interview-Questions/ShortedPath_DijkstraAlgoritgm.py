# Shorted Path Dijkstra Algoritgm:
# Along with the shortest distance, the shortest path also needed to be printed which made the problem quite difficult.

import heapq

def dijkstra_with_path(n, edges, source, destination):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    parent = [-1] * n
    dist[source] = 0

    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    # Reconstruct path
    if dist[destination] == float('inf'):
        return -1, []

    path = []
    current = destination
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return dist[destination], path

# Example
n = 5
edges = [
    (0, 1, 2),
    (1, 2, 4),
    (0, 3, 1),
    (3, 4, 3),
    (4, 2, 1)
]
source = 0
destination = 2

distance, path = dijkstra_with_path(n, edges, source, destination)
print("Shortest Distance:", distance)
print("Shortest Path:", path)
