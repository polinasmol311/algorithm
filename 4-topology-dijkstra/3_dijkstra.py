import heapq


def dijkstra_shortest_path():
    n, a, b = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for u in range(1, n + 1):
        parts = list(map(int, input().split()))
        k = parts[0]
        edges = parts[1:]
        for i in range(0, len(edges), 2):
            v = edges[i]
            w = edges[i + 1]
            graph[u].append((v, w))

    inf = float('inf')
    dist = [inf] * (n + 1)
    dist[a] = 0
    parent = [-1] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, a))

    while heap:
        current_dist, u = heapq.heappop(heap)

        if u == b:
            break

        if current_dist > dist[u]:
            continue

        for (v, w) in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[b] == inf:
        print(-1)
    else:
        path = []
        current = b
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
        print(dist[b])
        print(' '.join(map(str, path)))


dijkstra_shortest_path()
