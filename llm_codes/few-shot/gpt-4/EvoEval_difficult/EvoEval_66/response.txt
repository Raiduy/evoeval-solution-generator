def advancedDigitSum(s, t):
    """
    An optimized version of the advancedDigitSum function that uses list comprehensions and the built-in ord function
    to calculate the ASCII sum. This version avoids unnecessary iterations and function calls, which can be costly in terms of energy.
    """
    s_sum = sum(ord(c) for c in s if c.isupper())
    t_sum = sum(ord(c) for c in t if c.islower())
    return s_sum, t_sum