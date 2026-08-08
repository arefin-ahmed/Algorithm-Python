def dijkstra(graph, source):

    INF = 999999

    # Set initial distances
    distance = {}

    for vertex in graph:
        distance[vertex] = INF

    # Store previous vertex
    parent = {}

    for vertex in graph:
        parent[vertex] = None

    # Store visited vertices
    visited = []

    # Source distance is 0
    distance[source] = 0

    # Dijkstra algorithm
    for i in range(len(graph)):

        # Find the vertex with minimum distance
        min_distance = INF
        current = None

        for vertex in graph:

            if vertex not in visited:
                if distance[vertex] < min_distance:
                    min_distance = distance[vertex]
                    current = vertex

        # Mark current vertex as visited
        visited.append(current)

        # Check all neighboring vertices
        for neighbor, weight in graph[current]:

            new_distance = distance[current] + weight

            # Update distance if shorter path is found
            if new_distance < distance[neighbor]:

                distance[neighbor] = new_distance
                parent[neighbor] = current

    return distance, parent, visited


# -----------------------------
# Find shortest path
# -----------------------------

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


# -----------------------------
# Take graph input
# -----------------------------

graph = {}

n = int(input("Enter number of vertices: "))

print("Enter vertex names:")

for i in range(n):

    vertex = input("Vertex " + str(i + 1) + ": ")

    graph[vertex] = []


# Number of edges
m = int(input("Enter number of directed edges: "))

print("\nEnter edges in this format:")
print("Source Destination Weight")

for i in range(m):

    u, v, w = input("Edge " + str(i + 1) + ": ").split()

    w = int(w)

    graph[u].append((v, w))


# Source vertex
source = input("\nEnter source vertex: ")


# Run Dijkstra
distance, parent, visited = dijkstra(graph, source)


# -----------------------------
# Display result
# -----------------------------

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
        " -> ".join(path)
    )