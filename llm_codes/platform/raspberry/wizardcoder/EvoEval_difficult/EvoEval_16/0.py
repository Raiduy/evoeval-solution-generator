
def count_distinct_characters_substrings(string: str, length: int) -> dict:
    if length > len(string):
        return {}

    result = {}
    for i in range(len(string)):
        substring = string[i:i+length]
        if len(substring) < length:
            break
        result[substring] = len(set(substring))
    return result
