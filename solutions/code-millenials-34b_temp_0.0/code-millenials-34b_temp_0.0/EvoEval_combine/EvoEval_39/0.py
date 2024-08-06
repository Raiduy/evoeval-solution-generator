def smallest_change_and_sum(arr, x, y):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
    if n % 2 != 0:
        changes += 1
    return changes + x + y