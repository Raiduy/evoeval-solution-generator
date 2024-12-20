def find_palindrome_substrings(s: str):
    """
    Given a string, find all unique substrings that are palindromes.
    
    A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
    
    Return a list of all unique palindrome substrings, sorted in ascending order.

    >>> find_palindrome_substrings('racecar')
    ['a', 'aceca', 'c', 'cec', 'e', 'r', 'racecar']

    >>> find_palindrome_substrings('madam')
    ['a', 'ada', 'd', 'm', 'madam']

    >>> find_palindrome_substrings('civic')
    ['c', 'civic', 'i', 'ivi', 'v']

    >>> find_palindrome_substrings('hello')
    ['e', 'h', 'l', 'll', 'o']

    >>> find_palindrome_substrings('hannah')
    ['a', 'anna', 'h', 'hannah', 'n', 'nn']
    """
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return sorted(list(palindromes))