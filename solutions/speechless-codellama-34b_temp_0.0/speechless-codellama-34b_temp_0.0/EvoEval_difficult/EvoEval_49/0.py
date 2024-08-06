def modp(n: int, p: int, m: int) -> int:
    if m % p == 0:
        return -1
    result = pow(2, n, p) + m
    return result % p