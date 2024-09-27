
def decimal_to_binary(decimal, padding_length):
    # Check for invalid inputs
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or padding_length <= 0:
        return "Invalid Input"
    
    # Convert decimal to binary and remove the '0b' prefix
    binary_str = bin(decimal)[2:]
    
    # Check if the binary representation is longer than the padding length
    if len(binary_str) > padding_length:
        return "Padding length is too small"
    
    # Pad the binary string with leading zeros to reach the required length
    padded_binary_str = binary_str.zfill(padding_length)
    
    # Add the 'db' characters at the beginning and end
    result = f"db{padded_binary_str}db"
    
    return result
