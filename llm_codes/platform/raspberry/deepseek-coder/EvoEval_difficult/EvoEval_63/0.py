
def customFibFib(n: int, startSequence: list, p: int):
    # Ensure the startSequence has exactly 3 elements
    if len(startSequence) != 3:
        raise ValueError("startSequence must contain exactly 3 elements")
    
    # Handle the base cases directly
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]
    
    # Initialize the first three elements of the sequence
    a, b, c = startSequence
    
    # Iterate to compute the n-th element
    for i in range(3, n + 1):
        # Calculate the next element in the sequence
        next_value = a + b + c
        
        # Check if the next value exceeds the limit
        if next_value > p:
            return 'Limit Exceeded'
        
        # Update the sequence values for the next iteration
        a, b, c = b, c, next_value
    
    # Return the n-th element
    return c

# Test cases
