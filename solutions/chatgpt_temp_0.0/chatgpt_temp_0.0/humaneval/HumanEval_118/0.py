
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word = word.strip(consonants)
    if len(word) < 3:
        return ""
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i]
    return ""
