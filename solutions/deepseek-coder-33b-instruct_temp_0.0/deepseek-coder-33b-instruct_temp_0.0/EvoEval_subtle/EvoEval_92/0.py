
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the absolute values of other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  
    """
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == abs(y) + abs(z) or y == abs(x) + abs(z) or z == abs(x) + abs(y):
            return True
        else:
            return False
    else:
        return False