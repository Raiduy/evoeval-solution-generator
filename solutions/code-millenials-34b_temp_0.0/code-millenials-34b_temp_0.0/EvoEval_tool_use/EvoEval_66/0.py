def is_upper(c):
    """Helper Function: Check if the given character is uppercase.
    
    Args:
        c (str): Single character string to be checked.
    
    Returns:
        bool: True if the character is uppercase, False otherwise.
    """
    return c.isupper()

def is_lower(c):
    """Helper Function: Check if the given character is lowercase.
    
    Args:
        c (str): Single character string to be checked.
    
    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return c.islower()

def char_to_ascii(c):
    """Helper Function: Convert a character to its ASCII value.
    
    Args:
        c (str): Single character string to be converted.
    
    Returns:
        int: ASCII value of the character.
    """
    return ord(c)
def stringParse(s):
    upper_sum = 0
    lower_sum = 0
    for c in s:
        if is_upper(c):
            upper_sum += char_to_ascii(c)
        elif is_lower(c):
            lower_sum += char_to_ascii(c)
    return (upper_sum, lower_sum)