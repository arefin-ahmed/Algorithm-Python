INF = 999999

# Number of nodes
n = 5

# Given adjacency matrix
# 0 = no edge except diagonal
graph = [
    [0, 4, 2, 0, 0],
    [0, 0, 5, 10, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0]
]

# Source node
src = 0

# Convert 0 to INF (except diagonal)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and i != j:
            graph[i][j] = INF

# Initialize arrays
dist = graph[src].copy()
visited = [0] * n

dist[src] = 0
visited[src] = 1

# Dijkstra Algorithm
for c in range(1, n):

    # Pick the unvisited node with smallest distance
    minimum = INF
    next_node = -1

    for i in range(n):
        if not visited[i] and dist[i] < minimum:
            minimum = dist[i]
            next_node = i

    visited[next_node] = 1

    # Update neighbors
    for i in range(n):
        if (not visited[i] and
            dist[next_node] + graph[next_node][i] < dist[i]):

            dist[i] = dist[next_node] + graph[next_node][i]


# Print result
print("Shortest distances from node", src, ":")

for i in range(n):
    if dist[i] == INF:
        print(src, "→", i, "= No Path")
    else:
        print(src, "→", i, "=", dist[i])