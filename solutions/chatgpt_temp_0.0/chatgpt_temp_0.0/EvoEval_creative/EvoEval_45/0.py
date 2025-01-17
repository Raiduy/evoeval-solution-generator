def find_castle(arr):
    n = len(arr)
    if n == 0:
        return 0
    left_count = [1] * n
    right_count = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left_count[i] = left_count[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right_count[i] = right_count[i + 1] + 1
    max_hills = 0
    for i in range(n):
        max_hills = max(max_hills, left_count[i] + right_count[i] - 1)
    return max_hills