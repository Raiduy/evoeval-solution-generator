
def correct_bracketing_advanced(brackets: str) -> bool:
    """
    brackets is a string comprising "(", ")", "{", "}", "[", "]".
    return True if every opening bracket has a corresponding closing bracket of the same type and is correctly nested. 
    The bracket types must not intersect with one another.
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in brackets:
        if char in matching_bracket.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_bracket:
            # If it's a closing bracket, check if it matches the top of the stack
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False
    
    # If the stack is empty, all brackets were matched correctly
    return not stack

