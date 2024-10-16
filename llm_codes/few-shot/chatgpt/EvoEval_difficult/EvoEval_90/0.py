def next_smallest_and_largest(lst):
    """
    An optimized function to find the 2nd smallest and 2nd largest elements in a list without sorting.
    """
    if len(lst) < 2:
        return None, None

    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_smallest == float('inf') or second_largest == float('-inf'):
        return None, None

    return second_smallest, second_largest