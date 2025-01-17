

def fibfib(n: int):
    """This function calculates the n-th element of the FibFib sequence.
    The FibFib sequence is defined as:
    fibfib(0) = 0,
    fibfib(1) = 0,
    fibfib(2) = 1,
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    It returns the n-th element of this sequence.
    
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        (a, b, c) = (0, 0, 1)
        for _ in range(n - 2):
            (a, b, c) = (b, c, a + b + c)
        return c