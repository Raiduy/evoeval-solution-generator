from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from a given list preserving the original order.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers