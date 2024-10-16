def change_base(x: int, base: int) -> str:
    """Converts integer x to a different numerical base.
    Returns the conversion as a string.
    The base is less than 10.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    digits.reverse()
    return ''.join(digits)