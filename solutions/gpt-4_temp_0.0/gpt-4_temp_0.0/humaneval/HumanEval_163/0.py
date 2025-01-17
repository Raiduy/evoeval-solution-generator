
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is the smaller number
    if a > b:
        a, b = b, a

    # Generate list of even numbers between a and b
    return [i for i in range(a, b+1) if i in [2, 4, 6, 8]]
