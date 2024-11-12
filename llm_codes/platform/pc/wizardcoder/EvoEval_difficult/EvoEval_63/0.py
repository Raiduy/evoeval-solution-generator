
def customFibFib(n: int, startSequence: list, p: int):
    # Create a dictionary to store the computed values
    computed_values = {0: startSequence[0], 1: startSequence[1]}, 2: startSequenceSequence[2]}

    # Check if the n-th value is already computed
    if n in computed_values:
        return computed_values[n]

    # If the n-th value is not already computed, compute it
    else:
        for i in range(3, n+1):
            computed_values[i] = computed_values[i-1] + computed_values[i-2] + computed_values[i-3]]

            # Check if the sum at any point exceeds the positive integer 'p'
            if computed_values[i] > p:
                return 'Limit Exceeded'

        # Return the n-th computed value
        return computed_values[n]
