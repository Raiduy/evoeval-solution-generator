from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    groups = paren_string.split()
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        depths.append(max_depth)
    return depths