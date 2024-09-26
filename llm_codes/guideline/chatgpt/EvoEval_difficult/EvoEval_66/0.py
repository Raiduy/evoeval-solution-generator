def advancedDigitSum(s, t):
    sum_uppercase = 0
    sum_lowercase = 0
    
    for char in s:
        if char.isupper():
            sum_uppercase += ord(char)
    
    for char in t:
        if char.islower():
            sum_lowercase += ord(char)
    
    return (sum_uppercase, sum_lowercase)