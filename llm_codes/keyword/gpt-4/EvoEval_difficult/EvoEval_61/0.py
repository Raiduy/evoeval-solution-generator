
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for bracket in brackets:
        if bracket in bracket_map:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != bracket_map[stack.pop()]:
            return False

    return len(stack) == 0
