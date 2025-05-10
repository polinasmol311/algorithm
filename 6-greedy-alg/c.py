n = int(input())
interval = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[1])

right = -1
count = 0
for l, r in interval:
    if l >= right:
        count += 1
        right = r

print(count)