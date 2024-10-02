
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in bracket_map.values():  # if it's an opening bracket
            stack.append(bracket)
        elif bracket in bracket_map.keys():  # if it's a closing bracket
            if stack == [] or bracket_map[bracket] != stack.pop():
                return False
    return stack == []
