
def advancedDigitSum(s, t):
    sum_uppercase = sum(ord(char) for char in s if char.isupper())
    sum_lowercase = sum(ord(char) for char in t if char.islower())
    
    return (sum_uppercase, sum_lowercase)