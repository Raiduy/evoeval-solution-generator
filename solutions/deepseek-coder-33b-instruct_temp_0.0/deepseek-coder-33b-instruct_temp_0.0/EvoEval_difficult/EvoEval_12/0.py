from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    longest_substring = None
    longest_substring_index = None
    max_length = 0
    for (i, string) in enumerate(strings):
        string = string.lower()
        for j in range(len(string)):
            if string[j] in vowels:
                for k in range(j + 1, len(string) + 1):
                    substring = string[j:k]
                    if substring[0] in vowels and len(substring) > max_length:
                        max_length = len(substring)
                        longest_substring = substring
                        longest_substring_index = i
    return (longest_substring, longest_substring_index)