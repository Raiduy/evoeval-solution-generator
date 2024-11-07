
def next_smallest_and_largest(lst):
    if len(lst) < 2:
        return (None, None)

    smallest = second_smallest = float('inf')
    second_largest = smallest

    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest > num > smallest:
            second_smallest = num

        if num > second_largest:
            second_largest = num

    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None

    return (second_smallest, second_largest)
