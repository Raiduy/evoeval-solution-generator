
def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D', 'F']
    count = 0
    for char in num:
        if char not in primes:
            count += 1
    return count