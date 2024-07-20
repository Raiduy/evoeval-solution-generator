from typing import List, Tuple

def all_prefix_suffix_pairs(string: str, min_length: int) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(len(string)):
        for j in range(i + min_length, len(string)):
            prefix = string[:i]
            suffix = string[j:]
            if len(prefix) >= min_length and len(suffix) >= min_length:
                pairs.append((prefix, suffix))
    pairs.sort(key=lambda x: (len(x[0]) + len(x[1]), x))
    return pairs