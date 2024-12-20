
def fibfib(n: int):
    if n < 0:
        raise ValueError('n must be a non-negative integer')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0
    else:
        (a, b, c) = (0, 0, 1)
        for _ in range(3, n + 1):
            (a, b, c) = (b, c, a + b + c)
        return c