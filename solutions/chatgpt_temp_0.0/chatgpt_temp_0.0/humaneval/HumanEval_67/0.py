
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    """
    # Split the string into individual words
    words = s.split()

    # Initialize variables to store the counts of apples, oranges, and mangoes
    apples = 0
    oranges = 0
    mangoes = 0

    # Iterate through the words and update the counts accordingly
    for word in words:
        if word == "apples":
            apples = int(words[words.index(word) - 1])
        elif word == "oranges":
            oranges = int(words[words.index(word) - 1])

    # Calculate the number of mangoes
    mangoes = n - apples - oranges

    return mangoes
