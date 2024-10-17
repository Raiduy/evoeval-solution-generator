
def decimal_to_binary(decimal, padding_length):
    # Validate inputs
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length <= 0:
        return "Invalid Input"
    
    # Convert decimal to binary
    binary_str = bin(decimal)[2:]  # bin() returns a string like '0b1010', so we slice off the '0b'
    
    # Check if the binary representation fits within the padding length
    if len(binary_str) > padding_length:
        return "Padding length is too small"
    
    # Pad the binary string with leading zeros
    padded_binary_str = binary_str.zfill(padding_length)
    
    # Add 'db' at the beginning and end
    result = f"db{padded_binary_str}db"
    
    return result

# Example usage:
