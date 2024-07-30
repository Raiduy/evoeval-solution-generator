    if s == 'below':
        for i, num in enumerate(l):
            if num >= t1:
                return i
    elif s == 'above':
        for i, num in enumerate(l):
            if num <= t2:
                return i
    else:
        return -1
    return True