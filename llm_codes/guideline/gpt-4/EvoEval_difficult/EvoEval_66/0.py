
def advancedDigitSum(s, t):
    # Initialize the sums
    sum_s = 0
    sum_t = 0

    # Calculate the sum for 's'
    for char in s:
        if char.isupper():
            sum_s += ord(char)

    # Calculate the sum for 't'
    for char in t:
        if char.islower():
            sum_t += ord(char)

    # Return the sums as a tuple
    return (sum_s, sum_t)
