def correct_bracketing_advanced(brackets: str):
    stack = []
    opening = set(["(", "{", "["])
    closing = set([")", "}", "]"])
    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if not stack or stack[-1] != bracket_pairs[bracket]:
                return False
            stack.pop()

    return not stack

