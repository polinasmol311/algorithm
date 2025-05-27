def can_load(weights, k, capacity):
    mas = [0] * k
    for w in sorted(weights, reverse=True):
        flag = False
        for i in range(k):
            if mas[i] + w <= capacity:
                mas[i] += w
                flag = True
                break
        if not flag:
            return False
    return True


def min_max_capacity(n, k, weights):
    low = max(weights)
    high = sum(weights)

    while low < high:
        mid = (low + high) // 2
        if can_load(weights, k, mid):
            high = mid
        else:
            low = mid + 1

    return low


n, k = map(int, input().split())
weights = list(map(int, input().split()))
print(min_max_capacity(n, k, weights))
