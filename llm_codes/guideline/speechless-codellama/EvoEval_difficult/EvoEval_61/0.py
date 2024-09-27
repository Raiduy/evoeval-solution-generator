
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    for bracket in brackets:
        if bracket in bracket_map:
            stack.append(bracket)
        elif stack and stack[-1] == bracket_map[bracket]:
            stack.pop()
        else:
            return False
    return not stack
