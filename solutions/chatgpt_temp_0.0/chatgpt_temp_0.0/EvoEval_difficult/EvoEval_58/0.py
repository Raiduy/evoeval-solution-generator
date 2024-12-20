def common(l1: list, l2: list, n: int):
    common_strings = list(set(l1) & set(l2))
    common_strings.sort(key=lambda x: (len(x), l1.index(x)))
    return common_strings[:n]