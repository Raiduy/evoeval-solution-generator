
def advancedDigitSum(s, t):
    """
    Calculate the sum of ASCII codes for uppercase characters in 's' and lowercase characters in 't'.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    tuple: A tuple containing the sum of ASCII codes for uppercase characters in 's' and lowercase characters in 't'.
    """
    # Initialize sums
    sum_s = 0
    sum_t = 0
    
    # Loop through each character in 's'
    for char in s:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            sum_s += ord(char)  # Add ASCII value to sum_s
    
    # Loop through each character in 't'
    for char in t:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            sum_t += ord(char)  # Add ASCII value to sum_t
    
    return (sum_s, sum_t)

