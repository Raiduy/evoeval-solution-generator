

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


if __name__ == '__main__':
    inputs = [[5, [-1, 0, 1], 1000], [8, [0, 1, 2], 5], [1, [1, 1, 2], 1000], [10, [0, 0, 1], 100000], [20, [-1, 2, 3], 1000000], [15, [1, 1, 1], 50000], [25, [3, 5, 8], 300000], [30, [-1, -2, -3], 100000], [7, [2, 1, 3], 500000], [12, [0, -1, -2], 200000], [18, [2, 0, 2], 10000], [0, [1, 2, 3], 1000], [22, [-3, -5, -8], 500000], [17, [1, 0, -1], 250000], [13, [0, 0, 0], 1000], [6, [1, 2, 3], 1000], [10, [0, 1, 2], 500], [0, [1, 2, 3], 1000], [15, [2, 5, 7], 10000], [20, [-1, 1, 2], 100000], [3, [1, 1, 2], 10], [12, [3, 4, 5], 1000], [7, [0, 0, 1], 100], [4, [2, 3, 5], 50], [9, [1, -1, 1], 1000], [0, [0, 0, 0], 1000], [1, [1, 1, 1], 1], [2, [-1, -1, -1], 1], [50, [1, 1, 2], 10000], [3, [5, 5, 5], 10], [4, [-5, -5, -5], 5], [100, [0, 0, 0], 1000], [1000, [1, 2, 3], 100000], [5000, [1, 1, 1], 1000000], [10, [10, 10, 10], 100], [0, [100, 200, 300], 1000], [1, [1000, 2000, 3000], 5000], [2, [10000, 20000, 30000], 100000], [50, [0, 1, 2], 1000000000], [20, [-5, 10, -15], 1000], [30, [1, 2, 3], 500], [0, [100, 200, 300], 1000], [10, [100, 200, 300], 100000], [15, [1, 1, 1], 100], [25, [3, 2, 1], 50000], [35, [-1, -2, -3], 1000], [45, [10, 20, 30], 500000], [55, [5, -5, 10], 10000000], [20, [1, 2, 3], 100000], [30, [-2, 0, 2], 1000000], [15, [0, 0, 0], 0], [25, [-1, -1, -1], 10], [35, [5, 5, 5], 500], [45, [-10, 0, 10], 10000], [100, [1, 1, 1], 100000000], [50, [0, 1, 1], 50000], [75, [1, 2, 3], 10000000], [40, [-1, -2, -3], 1000]]
    number_of_executions = 3495145
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = customFibFib(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1

