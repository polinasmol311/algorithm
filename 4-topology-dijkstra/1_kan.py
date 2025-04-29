from collections import deque


def topological_sort_bfs():
    n = int(input())

    graph = {i: [] for i in range(1, n + 1)}
    in_degree = [0] * (n + 1)

    for u in range(1, n + 1):
        parts = list(map(int, input().split()))
        k = parts[0]
        neighbors = parts[1:]
        graph[u] = neighbors
        for v in neighbors:
            in_degree[v] += 1

    queue = deque()
    for u in range(1, n + 1):
        if in_degree[u] == 0:
            queue.append(u)

    topo_order = []
    processed = 0

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        processed += 1

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if processed != n:
        print(-1)
    else:
        print(" ".join(map(str, topo_order)))


topological_sort_bfs()
