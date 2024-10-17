
def customFibFib(n: int, startSequence: list, p: int):
    """
    Compute the n-th element of the CustomFibFib sequence with the given starting sequence and limit p.

    :param n: The position in the sequence to compute.
    :param startSequence: A list of three integers [a, b, c] representing the starting values.
    :param p: The limit for the sequence values.
    :return: The n-th element of the sequence or 'Limit Exceeded' if the sum exceeds p.
    """
    if n < 3:
        return startSequence[n]

    # Initialize the first three elements of the sequence
    a, b, c = startSequence

    # Iteratively compute the sequence up to the n-th element
    for i in range(3, n + 1):
        next_value = a + b + c
        if next_value > p:
            return 'Limit Exceeded'
        # Shift the values to the left
        a, b, c = b, c, next_value

    return c

# Test cases
