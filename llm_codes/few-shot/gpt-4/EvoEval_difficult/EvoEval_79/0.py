def decimal_to_binary(decimal, padding_length):
    """
    An optimized implementation of the decimal_to_binary function.
    The function uses bitwise operations to convert the decimal number to binary, which is more efficient than
    using the built-in bin function or manual division and remainder calculations.
    """
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    binary = ""
    while decimal:
        binary = str(decimal & 1) + binary
        decimal >>= 1

    if len(binary) > padding_length:
        return "Padding length is too small"

    binary = binary.zfill(padding_length)
    return "db" + binary + "db"