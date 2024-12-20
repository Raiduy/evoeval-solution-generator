
def prime_vowel(string):
    if not is_prime(len(string)):
        return ''
    vowels = 'aeiouAEIOU'
    for i in range(len(string) - 2, 0, -1):
        if string[i] in vowels and string[i - 1] not in vowels and (string[i + 1] not in vowels):
            return string[i]
    return ''