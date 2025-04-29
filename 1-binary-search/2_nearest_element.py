# def nearest_element(n, x, arr):
#     low = 0
#     high = n - 1
#     closest_index = 0
#     min_diff = arr[0] - x
#
#     while low <= high:
#         mid = (low+high)//2
#         current_diff = arr[mid] - x
#
#         if current_diff < min_diff:
#             min_diff = current_diff
#             closest_index = mid
#         elif current_diff == min_diff:
#             if mid < closest_index:
#                 closest_index = mid
#
#         if arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return closest_index
#
def nearest_element(n, x, arr):
    left = 0
    right = n - 1
    closest_idx = -1
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        diff = abs(arr[mid] - x)

        if diff < min_diff:
            min_diff = diff
            closest_idx = mid
        elif diff == min_diff and mid < closest_idx:
            closest_idx = mid

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return closest_idx


n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(nearest_element(n, x, arr))
