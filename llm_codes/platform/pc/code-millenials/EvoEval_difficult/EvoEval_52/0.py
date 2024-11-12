
def below_above_threshold(l: list, t1: int, t2: int, s: str):
    if s == 'below':
        for i, n in enumerate(l):
            if n >= t1:
                return i
        return True
    elif s == 'above':
        for i, n in enumerate(l):
            if n <= t2:
                return i
        return True
    else:
        return -1
