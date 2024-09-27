
def correct_bracketing_advanced(brackets: str):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if not stack or bracket_map[bracket] != stack.pop():
                return False

    return not stack

