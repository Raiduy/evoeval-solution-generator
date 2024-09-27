
def customFibFib(n: int, startSequence: list, p: int):
    # Check if n is negative or if the sequence is not valid
    if n < 0 or len(startSequence) != 3:
        return 'Invalid Input'

    # If n is 0, 1, or 2, return the corresponding value from the start sequence
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]

    # Initialize the sequence with the start values
    sequence = startSequence

    # Iterate through the rest of the sequence
    for i in range(3, n+1):
        # Calculate the next value in the sequence
        next_value = sequence[i-1] + sequence[i-2] + sequence[i-3]

        # If the next value exceeds the limit, return 'Limit Exceeded'
        if next_value > p:
            return 'Limit Exceeded'

        # Add the next value to the sequence
        sequence.append(next_value)

    # Return the n-th value of the sequence
    return sequence[n]
