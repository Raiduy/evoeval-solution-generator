
def count_up_to(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(n, 0, -1):
        if is_prime(i):
            primes.append(i)
    return primes