
def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]

    fib_sequence = startSequence + [0] * (n - 2)
    for i in range(3, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3]
        if fib_sequence[i] > p:
            return 'Limit Exceeded'

    return fib_sequence[n]
