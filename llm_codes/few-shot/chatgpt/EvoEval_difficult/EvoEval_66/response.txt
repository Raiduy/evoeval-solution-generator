def advancedDigitSum(s, t):
    """
    An optimized implementation of the advancedDigitSum function.
    """
    sum_s = sum(ord(char) for char in s if char.isupper())
    sum_t = sum(ord(char) for char in t if char.islower())
    
    return sum_s, sum_t