def is_vowel(char: str) -> bool:
    """ 
    Given a character, determine if it's a vowel.
    >>> is_vowel('a')
    True
    >>> is_vowel('b')
    False
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return char in vowels

def is_consonant(char: str) -> bool:
    """ 
    Given a character, determine if it's a consonant.
    >>> is_consonant('b')
    True
    >>> is_consonant('a')
    False
    """
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 
                  'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return char in consonants
def find_vowel_consonant_ratio(string: str) -> float:
    """ Given a string, find the ratio of vowels to consonants (rounded to 2 decimal places). The function should return -1 if no consonant is found. 
    The string only contains alphabets and is case insensitive.
    >>> find_vowel_consonant_ratio('Hello')
    0.67
    >>> find_vowel_consonant_ratio('Rhythm')
    0.0
    >>> find_vowel_consonant_ratio('AEIOU')
    -1
    """
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if is_vowel(char):
            vowel_count += 1
        elif is_consonant(char):
            consonant_count += 1
    if consonant_count == 0:
        return -1
    else:
        return round(vowel_count / consonant_count, 2)