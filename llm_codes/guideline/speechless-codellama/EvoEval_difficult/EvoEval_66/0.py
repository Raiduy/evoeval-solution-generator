
def advancedDigitSum(s, t):
    s_sum = 0
    t_sum = 0
    for char in s:
        if char.isupper():
            s_sum += ord(char)
    for char in t:
        if char.islower():
            t_sum += ord(char)
    return (s_sum, t_sum)
