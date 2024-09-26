
def decimal_to_binary(decimal, padding_length):
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    binary_num = bin(decimal)[2:]
    if len(binary_num) > padding_length:
        return "Padding length is too small"

    binary_num = '0' * (padding_length - len(binary_num)) + binary_num
    return f"db{binary_num}db"
