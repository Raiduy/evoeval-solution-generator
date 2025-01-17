def prime_sequences(n, m):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n) if is_prime(i)]
    sequences = [primes[i:i + m] for i in range(len(primes)) if len(primes[i:i + m]) == m]
    return sequences