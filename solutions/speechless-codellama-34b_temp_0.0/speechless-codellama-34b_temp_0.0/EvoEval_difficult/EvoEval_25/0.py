from typing import List, Tuple

def factorize_and_count(n: int) -> List[Tuple[int, int]]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append((i, count))
    if n > 1:
        factors.append((n, 1))
    return factors