
def below_above_threshold(l: list, t1: int, t2: int, s: str):
    if s == 'below':
        for i, val in enumerate(l):
            if val >= t1:
                return i
        return True
    elif s == 'above':
        for i, val in enumerate(l):
            if val <= t2:
                return i
        return True
    else:
        return -1
