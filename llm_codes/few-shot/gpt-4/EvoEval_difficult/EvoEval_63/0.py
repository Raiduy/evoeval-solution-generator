def customFibFib(n: int, startSequence: list, p: int):
    """
    An optimized implementation of the CustomFibFib sequence using dynamic programming to avoid redundant computations.
    """
    # Initialize the memoization array with the starting sequence
    fib = startSequence[:]

    # Compute the rest of the sequence
    for i in range(3, n + 1):
        next_val = fib[i - 1] + fib[i - 2] + fib[i - 3]
        # Check if the limit is exceeded
        if next_val > p:
            return 'Limit Exceeded'
        fib.append(next_val)

    return fib[n]