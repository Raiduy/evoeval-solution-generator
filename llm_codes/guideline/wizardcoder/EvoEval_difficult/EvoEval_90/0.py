
def next_smallest_and_largest(lst):
    if len(lst) < 2:
        return (None, None)
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
        if second_largest < num:
            second_largest = second_largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num # fix wrong variable name
    if second_smallest == float('inf'):
        smallest = None
    if second_largest == float('-inf'):
        second_largest = None
    return (second_smallest, second_largest)
