
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    last_char = txt[-1]
    if last_char.isalpha():
        if len(txt.split()[-1]) == 1:
            return True
    return False
