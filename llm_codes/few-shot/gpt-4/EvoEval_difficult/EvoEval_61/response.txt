def correct_bracketing_advanced(brackets: str):
    """
    An optimized version of the correct_bracketing_advanced function.
    The function uses a stack to keep track of the opening brackets and checks if the closing bracket matches the last opened one.
    """
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for bracket in brackets:
        if bracket in bracket_map:
            stack.append(bracket)
        elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
            return False

    return len(stack) == 0