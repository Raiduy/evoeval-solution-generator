
def decimal_to_binary(decimal, padding_length):
    # Check if inputs are valid
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    # Convert decimal to binary
    binary = bin(decimal)[2:]

    # Check if padding length is sufficient
    if len(binary) > padding_length:
        return "Padding length is too small"

    # Pad binary with '0's at the beginning
    binary = binary.zfill(padding_length)

    # Add extra characters at the beginning and end
    binary = "db" + binary + "db"

    return binary
