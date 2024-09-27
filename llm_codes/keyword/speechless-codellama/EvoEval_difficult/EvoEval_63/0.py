
def customFibFib(n: int, startSequence: list, p: int) -> int:
    if n < 0:
        return 0
    elif n < 3:
        return startSequence[n]
    else:
        a, b, c = startSequence
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
            if c > p:
                return 'Limit Exceeded'
        return c
