

def below_threshold(l: list, t: int):
    """Checks if all elements in list l are less than threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True