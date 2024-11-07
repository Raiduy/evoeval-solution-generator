
def count_distinct_characters_substrings(string: str, length: int) -> dict:
    if length > len(string):
        return {}

    substrings = [string[i:i+length] for i in range(len(string)-length+1)]
    distinct_characters = {substring: len(set(substring)) for substring in substrings} # extra )
    return distinct_characters
