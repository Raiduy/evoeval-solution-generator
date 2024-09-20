
from collections import defaultdict

def count_distinct_characters_substrings(string: str, length: int) -> dict:
    if length > len(string):
        return {}

    result = defaultdict(int)
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        distinct_chars = len(set(substring))
        result[substring] = distinct_chars

    return result

# Test cases
print(count_distinct_characters_substrings('xyzXYZabc', 3))
print(count_distinct_characters_substrings('Jerry', 2))
print(count_distinct_characters_substrings('Jerry', 6))
