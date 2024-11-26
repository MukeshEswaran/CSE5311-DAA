import heapq

# Dijkstra's Algorithm
def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        if current_dist > dist[u]:
            continue
        for neighbor, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
                heapq.heappush(priority_queue, (alt, neighbor))

    return dist, prev

# Bellman-Ford Algorithm
def bellman_ford(edges, source):
    vertices = set(u for u, v, w in edges) | set(v for u, v, w in edges)
    dist = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist, prev

# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    vertices = set(u for u, v in graph) | set(v for u, v in graph)
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    for u in vertices:
        dist[u][u] = 0
    for (u, v), w in graph.items():
        dist[u][v] = w

    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Test Graphs
graph_dijkstra = {
    's': [('u', 10), ('x', 5)],
    'u': [('v', 1), ('x', 2)],
    'v': [('y', 4)],
    'x': [('u', 3), ('v', 9), ('y', 2)],
    'y': [('s', 7), ('v', 6)],
}
edges_bellman_ford = [
    ('s', 'u', 10), ('s', 'x', 5),
    ('u', 'v', 1), ('u', 'x', 2),
    ('v', 'y', 4),
    ('x', 'u', 3), ('x', 'v', 9), ('x', 'y', 2),
    ('y', 's', 7), ('y', 'v', 6),
]
graph_floyd_warshall = {
    ('s', 'u'): 10, ('s', 'x'): 5,
    ('u', 'v'): 1, ('u', 'x'): 2,
    ('v', 'y'): 4,
    ('x', 'u'): 3, ('x', 'v'): 9, ('x', 'y'): 2,
    ('y', 's'): 7, ('y', 'v'): 6,
}

# Run all algorithms and print results
print("Dijkstra's Algorithm Results:")
dist, _ = dijkstra(graph_dijkstra, 's')
print(dist)

print("\nBellman-Ford Algorithm Results:")
dist, _ = bellman_ford(edges_bellman_ford, 's')
print(dist)

print("\nFloyd-Warshall Algorithm Results:")
dist = floyd_warshall(graph_floyd_warshall)
for u in dist:
    print(f"From {u}: {dist[u]}")
