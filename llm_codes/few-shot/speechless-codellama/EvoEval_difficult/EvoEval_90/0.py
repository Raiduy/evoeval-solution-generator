
def next_smallest_and_largest(lst):
    smallest = largest = None
    second_smallest = second_largest = None
    for num in lst:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest and num != smallest:
            second_smallest = num
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest and num != largest:
            second_largest = num
    return (second_smallest, second_largest)
