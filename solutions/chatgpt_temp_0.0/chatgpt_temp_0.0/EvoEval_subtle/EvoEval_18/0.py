
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    2
    """
    count = 0
    start = 0
    while start < len(string):
        index = string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + len(substring)
    return count