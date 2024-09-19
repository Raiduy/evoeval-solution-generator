
    if length > len(string):
        return {}
    result = {}
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        distinct_characters = set(substring)
        result[substring] = len(distinct_characters)
    return result
