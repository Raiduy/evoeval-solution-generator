def convert_to_binary(num: int) -> str:
    """
    This function takes in an integer and returns its binary equivalent as a string.
    """
    binary_num = bin(num).replace("0b", "")
    return binary_num

def is_palindrome(num: str) -> bool:
    """
    This function takes in a string and returns True if it is a palindrome, and False otherwise.
    """
    return num == num[::-1]
from typing import List

def binary_palindromes_in_range(lower: int, upper: int) -> List[int]:
    """
    This function takes in two integers, lower and upper, representing a range. 
    Your task is to return a list of all integers within that range (inclusive)
    whose binary representation is a palindrome. 

    For example, binary representation of 9 is 1001, which is a palindrome.
    Hence, if the range includes 9, it should be in the returned list.

    Ignore any negative numbers. If lower is greater than upper, or any of them is negative, 
    return an empty list.

    >>> binary_palindromes_in_range(1, 10)
    [1, 3, 5, 7, 9]

    >>> binary_palindromes_in_range(11, 20)
    [15]
    """
    if lower < 0 or upper < 0 or lower > upper:
        return []
    palindromes = []
    for num in range(lower, upper + 1):
        binary_num = convert_to_binary(num)
        if is_palindrome(binary_num):
            palindromes.append(num)
    return palindromes