

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
        fib_sequence = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3] + fib_sequence[i - 4])
        return fib_sequence[n]