
def decimal_to_binary(decimal, padding_length):
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    binary = bin(decimal)[2:]
    if len(binary) > padding_length:
        return "Padding length is too small"
    
    binary = '0' * (padding_length - len(binary)) + binary
    return f"db{binary}db"
