from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2  # Increment divisor efficiently
    return factors
