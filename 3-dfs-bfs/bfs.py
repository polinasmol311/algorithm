from collections import deque


def bfs(n, adj):
    visited = [False] * (n + 1)
    queue = deque()
    result = []

    queue.append(1)
    visited[1] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


n = int(input())
adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    k = parts[0]
    neighbor = parts[1:]
    adj[i] = neighbor

print(" ".join(map(str, bfs(n, adj))))
