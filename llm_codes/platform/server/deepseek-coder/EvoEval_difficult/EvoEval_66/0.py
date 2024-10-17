
def advancedDigitSum(s, t):
    """
    Calculate the sum of ASCII codes for uppercase characters in 's' and lowercase characters in 't'.

    :param s: A string containing any characters.
    :param t: A string containing any characters.
    :return: A tuple (sum_s, sum_t) where sum_s is the sum of ASCII codes of uppercase characters in 's'
             and sum_t is the sum of ASCII codes of lowercase characters in 't'.
    """
    sum_s = sum(ord(char) for char in s if char.isupper())
    sum_t = sum(ord(char) for char in t if char.islower())
    
    return (sum_s, sum_t)

# Example usage:
