
def customFibFib(n: int, startSequence: list, p: int):
    # Create a memoization dictionary
    memo = {0: startSequence[0] % p, 1: startSequence[1] % p, 2: startSequence[2] % p}

    # Calculate the n-th element of the sequence
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2] + memo[i - 3] ) % p
        # Check if the sum at any point exceeds 'p'
        if memo[i] > p:
            return 'Limit Exceeded'

    return memo[n]
