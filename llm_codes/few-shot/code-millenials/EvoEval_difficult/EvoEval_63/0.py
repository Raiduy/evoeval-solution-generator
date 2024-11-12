def customFibFib(n: int, startSequence: list, p: int):
    # Create a dictionary to store computed values
    computed = {i: val for i, val in enumerate(startSequence)}

    for i in range(len(startSequence), n + 1):
        # Compute the next value
        next_val = computed[i - 1] + computed[i - 2] + computed[i - 3]

        # Check if the sum exceeds 'p'
        if next_val > p:
            return 'Limit Exceeded'

        # Update the dictionary
        computed[i] = next_val

    return computed[n]
