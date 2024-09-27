
def count_distinct_characters_substrings(string: str, length: int) -> dict:
    if length > len(string):
        return {}
    else:
        substrings = [string[i: i + length] for i in range(len(string) - length + 1)]
        return {substring: len(set(substring)) for substring in substrings}
