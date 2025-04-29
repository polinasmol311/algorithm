def dfs(n, adj):
    visited = [False] * (n + 1)
    stack = []
    result = []

    stack.append(1)
    visited[1] = True

    while stack:
        current = stack.pop()
        result.append(current)

        for neighbor in reversed(adj[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return result


n = int(input())
adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    k = parts[0]
    neighbor = parts[1:]
    adj[i] = neighbor

print(" ".join(map(str, dfs(n, adj))))
