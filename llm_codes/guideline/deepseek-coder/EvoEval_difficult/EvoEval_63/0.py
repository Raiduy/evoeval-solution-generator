
def customFibFib(n: int, startSequence: list, p: int):
    # Ensure the startSequence has exactly 3 elements
    if len(startSequence) != 3:
        raise ValueError("startSequence must contain exactly 3 elements")
    
    # Unpack the start sequence
    a, b, c = startSequence
    
    # Handle the base cases directly
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    
    # Initialize the first three values
    prev3, prev2, prev1 = a, b, c
    
    # Loop to compute the sequence up to the n-th element
    for i in range(3, n + 1):
        # Compute the next value in the sequence
        next_val = prev1 + prev2 + prev3
        
        # Check if the limit is exceeded
        if next_val > p:
            return 'Limit Exceeded'
        
        # Update the previous values for the next iteration
        prev3, prev2, prev1 = prev2, prev1, next_val
    
    # Return the n-th element
    return prev1

