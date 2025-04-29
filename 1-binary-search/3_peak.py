def peak(n, arr):
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


n = int(input())
arr = list(map(int, input().split()))
print(peak(n, arr))
