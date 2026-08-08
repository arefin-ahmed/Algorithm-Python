def dijkstra(graph, source):

    INF = 999999
    distance = {}

    for vertex in graph:
        distance[vertex] = INF

    parent = {}

    for vertex in graph:
        parent[vertex] = None

    visited = []

    distance[source] = 0

    for i in range(len(graph)):
        min_distance = INF
        current = None

        for vertex in graph:
            if vertex not in visited:
                if distance[vertex] < min_distance:
                    min_distance = distance[vertex]
                    current = vertex

        visited.append(current)

        for neighbor, weight in graph[current]:
            new_distance = distance[current] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current

    return distance, parent, visited


def find_path(parent, source, destination):

    path = []

    current = destination

    while current != None:
        path.append(current)

        if current == source:
            break

        current = parent[current]

    path.reverse()

    return path


graph = {}

n = int(input("Enter number of vertices: "))

print("Enter vertex names:")

for i in range(n):
    vertex = input("Vertex " + str(i + 1) + ": ")

    graph[vertex] = []


m = int(input("Enter number of directed edges: "))

print("\nEnter edges in this format:")
print("Source Destination Weight")

for i in range(m):
    u, v, w = input("Edge " + str(i + 1) + ": ").split()

    w = int(w)

    graph[u].append((v, w))


source = input("\nEnter source vertex: ")


distance, parent, visited = dijkstra(graph, source)


print("\nVisited order:")
print(" -> ".join(visited))

print("\nShortest distances and paths:")

for vertex in graph:
    path = find_path(parent, source, vertex)

    print(
        source,
        "->",
        vertex,
        ": Distance =",
        distance[vertex],
        ", Path =",
        " -> ".join(path),
    )
