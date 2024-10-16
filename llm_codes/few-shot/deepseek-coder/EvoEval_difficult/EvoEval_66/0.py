
def advancedDigitSum(s, t):
    """
    Optimized function to calculate the sum of ASCII codes of uppercase characters in 's'
    and lowercase characters in 't'.
    """
    sum_s = 0
    sum_t = 0
    
    # Calculate sum for string 's'
    for char in s:
        if 'A' <= char <= 'Z':
            sum_s += ord(char)
    
    # Calculate sum for string 't'
    for char in t:
        if 'a' <= char <= 'z':
            sum_t += ord(char)
    
    return (sum_s, sum_t)

