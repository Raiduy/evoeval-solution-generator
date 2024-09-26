
def correct_bracketing_advanced(brackets: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in bracket_map.values():  # opening brackets
            stack.append(bracket)
        elif bracket in bracket_map.keys():  # closing brackets
            if stack == [] or bracket_map[bracket] != stack.pop():
                return False
    return stack == []
