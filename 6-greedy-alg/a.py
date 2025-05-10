n, k = map(int, input().split())

costs = list(map(int, input().split()))
costs.sort()
total = 0
c = 0
for cost in costs:
    if total + cost <= k:
        total += cost
        c += 1
print(c)
