
def advancedDigitSum(s, t):
    # Calculate the sum of ASCII codes of the uppercase characters in 's'
    s_sum = sum(ord(c) for c in s if c.isupper())
    
    # Calculate the sum of ASCII codes of the lowercase characters in 't'
    t_sum = sum(ord(c) for c in t if c.islower())
    
    # Return the results as a tuple
    return (s_sum, t_sum)
