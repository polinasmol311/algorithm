import heapq

n = int(input())
tasks = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
total = 0
min_heap = []
for d, w in tasks:
    if len(min_heap) < d:
        heapq.heappush(min_heap, w)
        total += w
    else:
        if min_heap[0] < w:
            total += w - heapq.heappop(min_heap)
            heapq.heappush(min_heap, w)

print(total)
