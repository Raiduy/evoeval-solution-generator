from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from a given list preserving the original order.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 2, 3, 4]
    """
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result