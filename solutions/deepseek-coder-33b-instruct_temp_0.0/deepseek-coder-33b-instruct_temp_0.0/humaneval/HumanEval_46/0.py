

def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0
    for _ in range(n - 3):
        a, b, c, d = b, c, d, a + b + c + d

    return d
