
from typing import List
from math import factorial

def special_close_factorials(numbers: List[int], threshold: int) -> bool:
    """ 
    Check if in given list of numbers, are any two special factorials closer to each other than 
    given threshold. The special factorial (Brazilian factorial) is defined as n! * (n!-1! * (n!-2! * ... * 1! 
    where n > 0.

    For example:
    >>> special_close_factorials([2, 3], 10)
    False
    >>> special_close_factorials([1, 2, 3, 4], 100)
    True
    """
    special_factorials = [factorial(n) * factorial(n - 1) * factorial(n - 2) for n in numbers]
    for i in range(len(special_factorials)):
        for j in range(i + 1, len(special_factorials)):
            if abs(special_factorials[i] - special_factorials[j]) < threshold:
                return True
    return False