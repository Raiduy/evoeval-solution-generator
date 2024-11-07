
def customFibFib(n: int, startSequence: list, p: int):
    # Create a dictionary to store the computed values
    computed_values = {0: startSequence[0], 1: startSequence[1]}, 2: startSequenceSequence[2]}

    # Check if the n-th value is already computed
    if n in computed_values:
        return computed_values[n]

    # If the n-th value is not already computed, compute it
    else:
        computed_values[n] = customFibibFib(n-1, startSequence, p) + customFibFibibFib(n-2, startSequence, p) + customFibFibibFibib(n-3, startSequence, p p)

        # If the sum at any point exceeds the positive integer 'p', return 'Limit Exceeded'
        if computed_values[n] > p:
            return 'Limit Exceeded'

        # Otherwise, return the computed n-th value
        else:
            return computed_values[n]
