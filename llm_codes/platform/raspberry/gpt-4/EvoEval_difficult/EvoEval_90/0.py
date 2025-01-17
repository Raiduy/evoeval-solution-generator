
def next_smallest_and_largest(lst):
    if not lst or len(lst) < 2:
        return (None, None)

    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in lst:
        if num <= smallest:
            if num < smallest:
                second_smallest = smallest
                smallest = num
        elif num < second_smallest:
            second_smallest = num

        if num >= largest:
            if num > largest:
                second_largest = largest
                largest = num
        elif num > second_largest:
            second_largest = num

    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None

    return (second_smallest, second_largest)
