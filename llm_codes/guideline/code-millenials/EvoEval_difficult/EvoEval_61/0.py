
def correct_bracketing_advanced(brackets: str) -> bool:
    # Assigning to a variable
    opening_brackets = "({["
    closing_brackets = ")}]"
    stack = []
    
    for bracket in brackets:
        # Check if it is an opening bracket
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            # Check if it is a closing bracket
            if not stack:
                return False
            else:
                # Check if brackets are correctly nested
                if opening_brackets.index(stack.pop()) != closing_brackets.index(bracket):
                    return False
    
    # Check if all brackets are closed
    return not stack
