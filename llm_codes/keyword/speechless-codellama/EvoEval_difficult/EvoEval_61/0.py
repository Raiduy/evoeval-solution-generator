
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket in "([{":
            stack.append(bracket)
        elif bracket in ")]}":
            if not stack or brackets.index(bracket) != brackets.index(stack.pop()):
                return False
    return not stack
