
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise. The function should ignore white spaces in the string length calculation.
    Examples
    prime_length('Hello') == True
    prime_length(' a b c d c b a ') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    string = string.replace(' ', '')
    return is_prime(len(string))