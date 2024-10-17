
def advancedDigitSum(s, t):
    """
    Calculate the sum of ASCII codes for uppercase characters in 's' and lowercase characters in 't'.

    Args:
        s (str): The first input string.
        t (str): The second input string.

    Returns:
        tuple: A tuple containing the sum of ASCII codes for uppercase characters in 's' and lowercase characters in 't'.
    """
    # Initialize sums for both strings
    sum_s = 0
    sum_t = 0

    # Calculate the sum of ASCII codes for uppercase characters in 's'
    for char in s:
        if 'A' <= char <= 'Z':
            sum_s += ord(char)

    # Calculate the sum of ASCII codes for lowercase characters in 't'
    for char in t:
        if 'a' <= char <= 'z':
            sum_t += ord(char)

    return (sum_s, sum_t)

# Example usage:
