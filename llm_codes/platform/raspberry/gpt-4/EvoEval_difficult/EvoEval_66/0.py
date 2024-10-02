
def advancedDigitSum(s, t):
    # Get ASCII sum of uppercase characters in s
    s_sum = sum(ord(c) for c in s if c.isupper())
    
    # Get ASCII sum of lowercase characters in t
    t_sum = sum(ord(c) for c in t if c.islower())
    
    return (s_sum, t_sum)
