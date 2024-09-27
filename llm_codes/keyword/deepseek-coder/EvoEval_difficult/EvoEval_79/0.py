
def decimal_to_binary(decimal, padding_length):
    # Validate inputs
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length <= 0:
        return "Invalid Input"
    
    # Convert decimal to binary
    binary_str = bin(decimal)[2:]  # bin() returns a string prefixed with '0b', so we slice it off
    
    # Check if padding length is sufficient
    if len(binary_str) > padding_length:
        return "Padding length is too small"
    
    # Pad the binary string with leading zeros
    padded_binary_str = binary_str.zfill(padding_length)
    
    # Add the 'db' prefix and suffix
    result = f"db{padded_binary_str}db"
    
    return result

