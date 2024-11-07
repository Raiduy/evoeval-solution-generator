
def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]
    else:
        a, b, c = startSequence[0], startSequence[1], startSequence[2] # fixed wrong variable name
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
            if a > p:
                return 'Limit Exceeded'
        return a
