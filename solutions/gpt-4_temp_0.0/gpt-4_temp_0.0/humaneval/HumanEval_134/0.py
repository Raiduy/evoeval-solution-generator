
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if not txt:  # if the string is empty
        return False
    if txt[-1] == ' ':  # if the last character is a space
        return False
    if txt[-2] == ' ':  # if the second last character is a space
        return txt[-1].isalpha()  # return True if the last character is a letter, False otherwise
    return False
