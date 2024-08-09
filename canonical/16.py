    if length > len(string):
        return {}
    else:
        result = {}
        for i in range(len(string) - length + 1):
            substring = string[i : i + length]
            result[substring] = len(set(substring))
        return result