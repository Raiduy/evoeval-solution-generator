
def prime_length(string):
    """Return True if the length of the input string is a prime number, False otherwise."""

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_prime(len(string))