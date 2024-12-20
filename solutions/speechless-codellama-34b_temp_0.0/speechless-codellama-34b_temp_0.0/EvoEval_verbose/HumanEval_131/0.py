
def digits(n):
    product = 1
    has_odd_digit = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            has_odd_digit = True
    if not has_odd_digit:
        return 0
    return product