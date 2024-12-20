
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y."""
    if n < 2:
        return y
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return y
    return x