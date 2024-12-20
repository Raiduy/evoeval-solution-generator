
def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_n_minus_3 = 0
        fibfib_n_minus_2 = 0
        fibfib_n_minus_1 = 1
        for i in range(3, n + 1):
            fibfib_n = fibfib_n_minus_3 + fibfib_n_minus_2 - fibfib_n_minus_1
            fibfib_n_minus_3 = fibfib_n_minus_2
            fibfib_n_minus_2 = fibfib_n_minus_1
            fibfib_n_minus_1 = fibfib_n
        return fibfib_n