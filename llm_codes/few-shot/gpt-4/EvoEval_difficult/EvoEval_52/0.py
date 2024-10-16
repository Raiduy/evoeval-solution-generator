def below_above_threshold(l: list, t1: int, t2: int, s: str):
    """
    An optimized version of the function that uses early termination and numpy arrays for efficient computation.
    """
    import numpy as np

    l = np.array(l)
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