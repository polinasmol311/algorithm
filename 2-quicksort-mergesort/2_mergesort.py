def merge_sort(n, arr):
    if n <= 1:
        return arr
    else:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(len(left), left)
        merge_sort(len(right), right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# n = int(input())
# arr = list(map(int, input().split()))
# ans = merge_sort(n, arr)
# print(" ".join(map(str, ans)))
