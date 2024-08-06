
from typing import List

def max_close_element_difference(numbers: List[float], threshold: float) -> float:
    """
    Given a list of numbers and a threshold, find two elements that are closer to each other than the threshold and return their difference. If multiple pairs meet the criteria, return the maximum difference. If no such pairs exist, return 0.
    >>> max_close_element_difference([1.0, 2.0, 3.0], 0.5)
    0
    >>> max_close_element_difference([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    0.2
    >>> max_close_element_difference([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 5)
    4
    """
    max_difference = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if difference < threshold and difference > max_difference:
                max_difference = difference
    return max_difference