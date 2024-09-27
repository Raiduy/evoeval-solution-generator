
def customFibFib(n: int, startSequence: list, p: int):
    """
    Compute the n-th element of the CustomFibFib sequence with a given starting sequence and a limit p.

    :param n: The position in the sequence to compute.
    :param startSequence: A list of three integers [a, b, c] representing the starting values.
    :param p: The limit for the sum of the sequence elements.
    :return: The n-th element of the sequence or 'Limit Exceeded' if the sum exceeds p.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n < 3:
        return startSequence[n]
    
    a, b, c = startSequence
    
    for i in range(3, n + 1):
        next_value = a + b + c
        if next_value > p:
            return 'Limit Exceeded'
        a, b, c = b, c, next_value
    
    return c

