def correct_bracketing_advanced(brackets: str) -> bool:
    """
    brackets is a string comprising "(", ")", "{", "}", "[", "]".
    return True if every opening bracket has a corresponding closing bracket of the same type and is correctly nested. 
    The bracket types must not intersect with one another.
    """
    # Dictionary to hold the matching pairs of brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    for bracket in brackets:
        if bracket in matching_bracket.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(bracket)
        elif bracket in matching_bracket.keys():
            # If it's a closing bracket, check if it matches the top of the stack
            if stack and stack[-1] == matching_bracket[bracket]:
                stack.pop()
            else:
                return False
        else:
            # If the character is not a bracket, return False (though the problem guarantees only brackets)
            return False
    
    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0

# Test cases
