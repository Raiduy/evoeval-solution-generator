
from typing import List


def sort_numbers(numbers: str) -> str:
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: number_map[x], reverse=True)
    return ' '.join(numbers_list)