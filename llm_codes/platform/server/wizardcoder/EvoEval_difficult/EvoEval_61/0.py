def correct_bracketing_advanced(brackets: str):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']':'['}

    for bracket in brackets:
        if bracket in bracket_pairs:
            if stack and bracket_pairs[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return not stack
