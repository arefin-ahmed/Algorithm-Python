INF = 99999999

n = 5
graph = [
    [0, 4, 2, 0, 0],
    [0, 0, 5, 10, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4]
]

src = 0

for i in range (n):
    for j in range (n):
        if graph [i][j] == 0 and i!=j:
            graph [i][j] = INF

for i in range (n-1):
    dist = graph [src][i]
    visited = [0]

dist[src] = 0
visited[src] = 1

for c in range (1, n-1):
    min = INF
    next = -1

    for i in range (n-1):
        if not visited[i] and dist[i] < min:
            min = dist[i]
            next = i

    visited[next] = 1

    for i in range (n-1):
        if not visited [i] and dist [next] + graph [next][i] < dist[i]:
            dist[i] = dist[next] + graph[next][i]

print ("Shortest distance from node", src)
for i in range (n-1):
    if dist[i] == INF:
        print (src, "->" , i, "No Path")
    else:
        print (src, "->" , i , "=", dist[i])
