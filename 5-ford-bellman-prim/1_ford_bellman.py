inf = float('inf')

def bellman_ford(n, m, a, b, edges):
    dist = [inf] * (n + 1)
    prev = [-1] * (n + 1)
    dist[a] = 0

    # Основной цикл релаксации
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    neg = [False] * (n + 1)
    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            neg[v] = True

    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        for uu, vv, _ in edges:
            if uu == u and not visited[vv]:
                dfs(vv)

    for v in range(1, n + 1):
        if neg[v] and not visited[v]:
            dfs(v)

    if visited[b]:
        return -1

    if dist[b] == inf:
        return -1


    path = []
    current = b
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return dist[b], path

n, m, a, b = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

ans = bellman_ford(n, m, a, b, edges)
if ans == -1:
    print(-1)
else:
    distance, path = ans
    print(distance)
    print(" ".join(map(str, path)))
