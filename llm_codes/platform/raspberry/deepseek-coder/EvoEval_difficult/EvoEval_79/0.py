
def decimal_to_binary(decimal, padding_length):
    # Check for valid input
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length <= 0:
        return "Invalid Input"
    
    # Convert decimal to binary
    binary_representation = bin(decimal)[2:]  # bin() returns '0b...' so we slice off the '0b'
    
    # Check if the binary representation fits within the padding length
    if len(binary_representation) > padding_length:
        return "Padding length is too small"
    
    # Pad the binary representation with leading zeros
    padded_binary = binary_representation.zfill(padding_length)
    
    # Add the 'db' characters at the beginning and end
    formatted_binary = f"db{padded_binary}db"
    
    return formatted_binary

# Example usage:
