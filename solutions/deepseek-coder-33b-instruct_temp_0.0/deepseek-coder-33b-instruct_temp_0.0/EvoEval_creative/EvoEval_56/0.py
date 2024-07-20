def str_to_morse_code(s):
    morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    words = s.split(' ')
    morse_code_words = []
    for word in words:
        morse_code_chars = [morse_code_dict[char] for char in word]
        morse_code_words.append('/'.join(morse_code_chars))
    return ' / '.join(morse_code_words)