
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket in "([{":
            stack.append(bracket)
        elif bracket in ")]}":
            if not stack:
                return False
            if bracket == ")" and stack.pop() != "(":
                return False
            if bracket == "]" and stack.pop() != "[":
                return False
            if bracket == "}" and stack.pop() != "{":
                return False
    return not stack
