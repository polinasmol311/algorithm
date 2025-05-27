def heapify(arr, n, i):
    largest = i
    low = 2 * i + 1
    high = 2 * i + 2

    if low < n and arr[low] > arr[largest]:
        largest = low

    if high < n and arr[high] > arr[largest]:
        largest = high

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(n, arr):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


n = int(input())
arr = list(map(int, input().split()))
ans = (heapsort(n, arr))
print(" ".join(map(str, ans)))
