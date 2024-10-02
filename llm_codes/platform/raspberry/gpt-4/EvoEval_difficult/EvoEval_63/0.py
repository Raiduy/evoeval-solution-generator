
def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]

    fib_sequence = startSequence[:]

    for i in range(3, n + 1):
        next_value = sum(fib_sequence[-3:])
        if next_value > p:
            return 'Limit Exceeded'
        fib_sequence.append(next_value)

    return fib_sequence[-1]
