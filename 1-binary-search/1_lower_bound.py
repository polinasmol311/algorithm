def lower_bound(n, x, arr):
    low = 0
    high = n - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            result = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
    return result


n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(lower_bound(n, x, arr))
