def customFibFib(n: int, startSequence: list, p: int):
    """
    An optimized implementation of the CustomFibFib sequence calculation function.
    """
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]

    a, b, c = startSequence
    fib_values = [a, b, c]

    for i in range(3, n+1):
        next_val = fib_values[i-1] + fib_values[i-2] + fib_values[i-3]
        if next_val > p:
            return 'Limit Exceeded'
        fib_values.append(next_val)

    return fib_values[n]