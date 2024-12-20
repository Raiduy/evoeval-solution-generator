
def prod_signs(arr):
    if len(arr) == 0:
        return None
    abs_sum = sum((abs(num) for num in arr))
    sign_product = 1
    for num in arr:
        if num < 0:
            sign_product *= -1
        elif num == 0:
            sign_product = 0
    return abs_sum * sign_product