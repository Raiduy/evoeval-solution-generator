
def customFibFib(n: int, startSequence: list, p: int):
    # Create a dictionary to store the computed values
    computed_values = {0: startSequence[0], 1: startSequence[1]}, 2: startSequenceSequence[2]}

    # Iterate from 3 to n
    for i in range(3, n+1):
        # Compute the i-th value
        computed_values[i] = computed_values[i-1] + computed_values[i-2] + computed_values[i-3]

        # If the sum at any point exceeds 'p', return 'Limit Exceeded'
        if computed_values[i] > p:
            return 'Limit Exceeded'

    # Return the n-th computed value
    return computed_values[n]
