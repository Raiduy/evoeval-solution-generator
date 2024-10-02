
def correct_bracketing_advanced(brackets: str):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in mapping.values():
            stack.append(bracket)
        elif bracket in mapping.keys():
            if not stack or mapping[bracket] != stack.pop():
                return False
        else:
            return False

    return not stack

