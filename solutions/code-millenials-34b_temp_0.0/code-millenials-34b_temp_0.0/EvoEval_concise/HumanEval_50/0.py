
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Decodes a string encoded with encode_shift function.
    """
    return ''.join([chr((ord(ch) - 5 - ord('a')) % 26 + ord('a')) for ch in s])