
def move_one_ball(arr):
    if not arr:
        return True
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            if count > 1:
                return False
    if arr[-1] > arr[0]:
        count += 1
    return count <= 1