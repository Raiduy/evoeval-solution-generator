
def customFibFib(n: int, startSequence: list, p: int):
    # Check if n is less than the length of the start sequence
    if n < len(startSequence):
        return startSequence[n]

    # Initialize the list with the start sequence
    fib = startSequence[:]

    # Compute the next elements of the sequence
    for i in range(len(startSequence), n + 1):
        # Compute the next element
        next_element = fib[i - 1] + fib[i - 2] + fib[i - 3]

        # Check if the sum exceeds p
        if next_element > p:
            return 'Limit Exceeded'

        # Add the next element to the list
        fib.append(next_element)

    # Return the n-th element of the sequence
    return fib[n]
