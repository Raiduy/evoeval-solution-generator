
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start with 1 or end with 2.
    """
    if n == 1:
        return 2
    else:
        return 10 ** (n - 1) + 2 * 9 ** (n - 1) - 9 ** (n - 1)