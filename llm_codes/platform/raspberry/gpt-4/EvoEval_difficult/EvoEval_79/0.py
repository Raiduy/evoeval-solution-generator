
def decimal_to_binary(decimal, padding_length):
    # Check if the inputs are valid
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length < 0:
        return "Invalid Input"

    # Convert the decimal to binary
    binary = bin(decimal)[2:]

    # Check if the binary representation is longer than the padding_length
    if len(binary) > padding_length:
        return "Padding length is too small"

    # Pad the binary number with '0's at the beginning to reach the required 'padding_length'
    binary = binary.zfill(padding_length)

    # Add the extra characters 'db' at the beginning and at the end of the string
    binary = "db" + binary + "db"

    return binary
