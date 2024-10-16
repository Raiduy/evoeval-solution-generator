def decimal_to_binary(decimal, padding_length):
    """
    An optimized implementation of the decimal to binary conversion function.
    This implementation uses bitwise operations to convert decimal to binary efficiently.
    """
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    binary = bin(decimal)[2:]
    if len(binary) > padding_length:
        return "Padding length is too small"
    
    binary = binary.zfill(padding_length)
    return f"db{binary}db"