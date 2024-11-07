def correct_bracketing_advanced(brackets: str):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']':'['}

    for bracket in brackets:
        if bracket in bracket_pairs:
            if not stack or bracket_pairs[bracket] != stack.pop():
                return False
        else:
            stack.append(bracket)

    return not stack
