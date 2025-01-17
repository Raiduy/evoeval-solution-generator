
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = -(-num // 10 * 10 + num % 10)
        digits_sum = sum((int(digit) for digit in str(num)))
        if digits_sum > 0:
            count += 1
    return count