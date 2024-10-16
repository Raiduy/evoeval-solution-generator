def below_above_threshold(l: list, t1: int, t2: int, s: str):
    """
    Check if all numbers in the list 'l' are below or above the given thresholds based on the condition 's'.
    Return True if all numbers satisfy the condition, otherwise return the index of the first element that violates it.
    """
    if s == 'below':
        for i in range(len(l)):
            if l[i] >= t1:
                return i
        return True
    elif s == 'above':
        for i in range(len(l)):
            if l[i] <= t2:
                return i
        return True
    else:
        return -1