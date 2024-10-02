
def advancedDigitSum(s, t):
    # Initialize the sums
    sum_s = 0
    sum_t = 0

    # Iterate over the characters in s
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII value of the character to the sum
            sum_s += ord(char)

    # Iterate over the characters in t
    for char in t:
        # Check if the character is lowercase
        if char.islower():
            # Add the ASCII value of the character to the sum
            sum_t += ord(char)

    # Return the sums as a tuple
    return (sum_s, sum_t)
