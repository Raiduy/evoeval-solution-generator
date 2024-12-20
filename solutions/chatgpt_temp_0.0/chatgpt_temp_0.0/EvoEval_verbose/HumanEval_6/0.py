from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    groups = paren_string.split()
    for group in groups:
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()
        depths.append(max_depth)
    return depths