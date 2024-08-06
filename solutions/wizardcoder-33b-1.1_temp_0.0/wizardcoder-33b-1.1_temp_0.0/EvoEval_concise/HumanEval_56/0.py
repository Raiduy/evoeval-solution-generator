

def correct_bracketing(brackets: str):
    """
    Checks if each '<' has a matching '>' in the string.
    Assumes string consists only of '<' and '>' characters.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    count = 0
    for bracket in brackets:
        if bracket == '<':
            count += 1
        elif bracket == '>':
            if count == 0:
                return False
            count -= 1
    return count == 0