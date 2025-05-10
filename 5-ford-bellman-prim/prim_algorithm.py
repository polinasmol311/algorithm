import heapq


def prim():
    n, m = map(int, input().split())
    mas = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        mas[u].append((v, w))
        mas[v].append((u, w))

    visited = [False] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, 1, -1))
    total_weight = 0
    mst_edges = []

    while heap:
        weight, u, parent = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent, u))

        for v, w in mas[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v, u))

    if sum(visited[1:]) != n:
        print(-1)
    else:
        print(total_weight)
        mst_edges_sorted = sorted(mst_edges)
        edges_str = ' '.join(f'{u} {v}' for u, v in mst_edges_sorted)
        print(edges_str)


prim()
