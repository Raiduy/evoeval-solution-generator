
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the sum of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 10.
    multiply(19, 28) should return 17.
    multiply(2020, 1851) should return 1.
    multiply(14,-15) should return 9.
    """
    a_last_digit = abs(a) % 10
    b_last_digit = abs(b) % 10
    return a_last_digit + b_last_digit