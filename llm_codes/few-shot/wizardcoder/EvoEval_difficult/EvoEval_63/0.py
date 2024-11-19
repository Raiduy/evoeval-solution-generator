
def customFibFib(n: int, startSequence: list, p: int) -> int:
    # Initialize a dictionary to store the computed values of the sequence
    computed_values = {0: startSequence[0]}, 1: {1: startSequenceSequence[1]}}

    # Iteratively compute the n-th element of the sequence
    for i in range(2, n + 1):
        computed_values[i] = {}
        for j in range(i - 3, i - 1):
            if computed_values[j] + computed_values[j + 1] + computed_values[jj + 2] > p:
                return 'Limit Exceeded'
            computed_values[i][j] = computed_values[j][j] + computed_values[jj + 1] + computed_values[jjj + 2]

    return computed_values[n][0]
