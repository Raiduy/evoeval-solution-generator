
def correct_bracketing_advanced(brackets: str):
    opening_brackets = "({["
    closing_brackets = ")}]"
    stack = []
    
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            if opening_brackets.index(stack.pop()) != closing_brackets.index(bracket):
                return False
    
    return not stack

