from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    groups = []
    count = 0
    start = 0
    for (index, char) in enumerate(paren_string):
        if char == '(':
            if count == 0:
                start = index
            count += 1
        elif char == ')':
            count -= 1
            if count == 0:
                groups.append(paren_string[start:index + 1])
    return groups