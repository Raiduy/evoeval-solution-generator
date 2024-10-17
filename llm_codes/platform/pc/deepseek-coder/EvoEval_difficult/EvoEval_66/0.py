
def advancedDigitSum(s, t):
    # Initialize sums for both strings
    sum_s = 0
    sum_t = 0
    
    # Sum ASCII values of uppercase characters in string 's'
    for char in s:
        if char.isupper():
            sum_s += ord(char)
    
    # Sum ASCII values of lowercase characters in string 't'
    for char in t:
        if char.islower():
            sum_t += ord(char)
    
    # Return the results as a tuple
    return (sum_s, sum_t)

# Example usage:
