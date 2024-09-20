
def customFibFib(n: int, startSequence: list, p: int):
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]
    
    a, b, c = startSequence
    fib = [a, b, c]
    
    for i in range(3, n+1):
        next_fib = fib[i-1] + fib[i-2] + fib[i-3]
        if next_fib > p:
            return 'Limit Exceeded'
        fib.append(next_fib)
    
    return fib[n]

