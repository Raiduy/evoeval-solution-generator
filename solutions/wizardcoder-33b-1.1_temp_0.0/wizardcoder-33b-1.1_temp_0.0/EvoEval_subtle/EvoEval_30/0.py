
def get_positive(l: list):
    """Return only positive numbers in the list in ascending order.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [1, 2, 3, 3, 5, 9, 123]
    """
    return sorted([i for i in l if i > 0])