
def calculate_word_frequency(string: str) -> dict:
    """ Given a string, calculate the frequency of each word present in that string (regardless of case) and return a dictionary with words as keys and their frequencies as values. 
    Words are separated by spaces. Ignore punctuation.
    
    >>> calculate_word_frequency('Hello, World! Hello Again.')
    {'hello': 2, 'world': 1, 'again': 1}

    >>> calculate_word_frequency('This is a test. This is only a test.')
    {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
    """
    words = re.sub('[^\\w\\s]', '', string.lower()).split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency