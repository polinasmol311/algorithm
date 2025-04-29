def bubblesort(n, arr):
    for i in range(n):
        flag = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

                flag = True

        if not flag:
            break

    return arr


n = int(input())
arr = list(map(int, input().split()))
ans = (bubblesort(n, arr))
print(" ".join(map(str, ans)))
