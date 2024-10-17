
def decimal_to_binary(decimal, padding_length):
    """
    Converts a decimal number to a binary string with padding and extra 'db' characters.

    :param decimal: The decimal number to convert.
    :param padding_length: The desired length of the padded binary string.
    :return: The binary string with padding and 'db' characters, or an error message.
    """
    # Validate inputs
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length <= 0:
        return "Invalid Input"

    # Convert decimal to binary
    binary_str = bin(decimal)[2:]  # bin() returns '0b...' so we slice off the '0b'

    # Check if padding length is sufficient
    if len(binary_str) > padding_length:
        return "Padding length is too small"

    # Pad the binary string with leading zeros
    padded_binary_str = binary_str.zfill(padding_length)

    # Add the 'db' characters at the beginning and end
    formatted_binary_str = f"db{padded_binary_str}db"

    return formatted_binary_str

# Example usage:
