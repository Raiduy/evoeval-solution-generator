
import re


def prime_underscored_length(text):
    text = re.sub(' +', '_', text)
    return is_prime(len(text))