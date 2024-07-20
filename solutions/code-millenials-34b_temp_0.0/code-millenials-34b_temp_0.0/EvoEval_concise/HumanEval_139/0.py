def special_factorial(n):
    if n < 0:
        raise ValueError('n should be a positive integer')
    if n == 0:
        return 1
    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)
    return result