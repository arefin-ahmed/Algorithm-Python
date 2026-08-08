def dijkstra(graph, source):
    INF = float("inf")

    distance = {vertex: INF for vertex in graph}
    parent = {vertex: None for vertex in graph}
    visited = set()
    visit_order = []

    distance[source] = 0

    for _ in range(len(graph)):
        # Select the unvisited vertex with minimum distance
        u = min(
            (v for v in graph if v not in visited),
            key=lambda v: distance[v]
        )

        visited.add(u)
        visit_order.append(u)

        # Relax all outgoing edges
        for v, weight in graph[u]:
            new_distance = distance[u] + weight

            if new_distance < distance[v]:
                distance[v] = new_distance
                parent[v] = u

    return distance, parent, visit_order


def get_path(parent, source, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = parent[current]

    path.reverse()
    return " -> ".join(path)


# Take graph as input
graph = {}

n = int(input("Enter number of vertices: "))

print("Enter vertex names:")
for _ in range(n):
    vertex = input().strip()
    graph[vertex] = []

m = int(input("Enter number of directed edges: "))

print("Enter each edge like-> source destination weight")
for _ in range(m):
    u, v, w = input().split()
    graph[u].append((v, int(w)))

source = input("Enter source vertex: ").strip()

distance, parent, visit_order = dijkstra(graph, source)

print("\nVisited order:", " -> ".join(visit_order))
print("\nShortest distances and paths:")

for vertex in graph:
    path = get_path(parent, source, vertex)
    print(f"{source} -> {vertex}: distance = {distance[vertex]}, "
          f"path = {path}")