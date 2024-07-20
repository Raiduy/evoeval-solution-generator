

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that ends with a supplied string.
    Algorithm idea is simple:
    - Find the longest prefix of supplied string that is a palindrome.
    - Append to the start of the string reverse of a string suffix that comes after the palindromic prefix.
    """
    for i in range(len(string)):
        if is_palindrome(string[:i + 1]):
            return string + string[i + 1:][::-1]
    return string + string[::-1]