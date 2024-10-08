

def triples_sum_to_zero(l: list):
    """
    Check if there are three distinct elements in the given list of integers that sum to zero. If yes, return True, otherwise return False.
    """
    l.sort()
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return False