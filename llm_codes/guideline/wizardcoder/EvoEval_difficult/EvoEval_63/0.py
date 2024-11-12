
def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]
    else:
        a, b, c = startSequence[0], startSequenceSequence[1], startSequenceSequence[2]]
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
            if a > p or b > p or c > p:
                return 'Limit Exceeded'
        return a
