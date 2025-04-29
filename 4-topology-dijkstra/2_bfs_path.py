from collections import deque


def shortest_path_bfs():
    n, a, b = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for u in range(1, n + 1):
        parts = list(map(int, input().split()))
        graph[u] = parts[1:] if parts[0] > 0 else []

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    distance = [-1] * (n + 1)

    queue = deque()
    queue.append(a)
    visited[a] = True
    distance[a] = 0

    while queue:
        u = queue.popleft()

        if u == b:
            break

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.append(v)

    if distance[b] == -1:
        print(-1)

    else:
        path = []
        current = b
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
        print(distance[b])
        print(" ".join(map(str, path)))


shortest_path_bfs()
