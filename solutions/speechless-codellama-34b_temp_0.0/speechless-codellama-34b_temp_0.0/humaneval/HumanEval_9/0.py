from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    max_so_far = numbers[0]
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result
