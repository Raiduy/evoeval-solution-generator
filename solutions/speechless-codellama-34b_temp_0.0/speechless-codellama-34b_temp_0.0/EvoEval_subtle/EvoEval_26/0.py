
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = list(set(numbers))
    return unique_numbers[::-1]