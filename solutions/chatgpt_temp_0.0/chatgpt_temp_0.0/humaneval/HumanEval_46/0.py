

def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        fib = [0, 0, 2, 0]
        for i in range(4, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])
        return fib[n]
