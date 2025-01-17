
def fruit_distribution(s, n):
    """
    Given a string representing the number of apples and oranges, and an integer representing the total
    number of fruits in a basket, this function returns the number of mango fruits in the basket.
    The string format is "{number of apples} apples and {number of oranges} oranges". The function computes 
    the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.
    Examples:
    fruit_distribution("5 apples and 6 oranges", 19) -> 8
    fruit_distribution("0 apples and 1 oranges",3) -> 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 95
    fruit_distribution("100 apples and 1 oranges",120) -> 19
    """
    words = s.split()
    apples = int(words[0])
    oranges = int(words[2])
    mangoes = n - (apples + oranges)
    return mangoes