def ford_bellman():
    n, m, a, b = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    inf = float('inf')
    dist = [inf] * (n + 1)
    dist[a] = 0
    prev = [-1] * (n + 1)

    for _ in range(n - 1):
        flag = False
        for u, v, w in edges:
            if dist[u] != inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                flag = True
        if not flag:
            break

    neg_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[v] > dist[u] + w:
            neg_cycle = True
            break

    if dist[b] == inf or neg_cycle:
        print(-1)
    else:
        path = []
        current = b
        while current != -1:
            path.append(current)
            current = prev[current]
        path.reverse()

        print(dist[b])
        print(' '.join(map(str, path)))


ford_bellman()
