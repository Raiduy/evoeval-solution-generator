
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] in consonants and (word[i + 1] in consonants):
            return word[i]
    return ''