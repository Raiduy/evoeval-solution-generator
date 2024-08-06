
def median(l: list):
    """Return median of elements in the list l, but if the list is empty, return 0 instead.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    >>> median([])
    0
    """
    if len(l) == 0:
        return 0
    sorted_list = sorted(l)
    mid_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]