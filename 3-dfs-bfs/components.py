from collections import deque


def count_components_bfs(n, adj):
    visited = [False] * (n + 1)
    components = 0

    for vertex in range(1, n + 1):
        if not visited[vertex]:
            components += 1

            queue = deque()
            queue.append(vertex)
            visited[vertex] = True

            while queue:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    return components


n = int(input())
adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    adj[i] = parts[1:]

print(count_components_bfs(n, adj))
