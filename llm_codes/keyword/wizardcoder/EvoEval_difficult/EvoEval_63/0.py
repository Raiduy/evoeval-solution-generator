
def customFibFib(n: int, startSequence: list, p: int):
    if n < len(startSequence):
        return startSequence[n]
    sequence = startSequence + [0] * (n - len(startSequence) + 1) # fix typo startSequenceSequence
    for i in range(len(startSequence), n + 1):
        sequence[i] = sum(sequence[i-j] for j in range(1, 4))
        if sequence[i] > p:
            return 'Limit Exceeded'
    return sequence[n]
