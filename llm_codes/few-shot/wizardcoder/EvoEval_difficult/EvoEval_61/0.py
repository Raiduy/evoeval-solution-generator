def correct_bracketing_advanced(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(' or bracket == '[' or bracket == '{':
            stack.append(bracket)
        elif bracket == ')' or bracket == ']' or bracket == '}':
            if not stack:
                return False
            top_element = stack.pop()
            if bracket == ')' and top_element != '(':
                return False
            if bracket == ']' and top_element != '[':
                return False
            if bracket == '}' and top_element != '{':
                return False
    if stack:
        return False
    return True 
