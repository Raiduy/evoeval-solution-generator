
def next_smallest_and_largest(lst):
    if len(lst) < 2:
        return (None, None)
    
    # Initialize variables to track the smallest, 2nd smallest, largest, and 2nd largest
    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')
    
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
    
    # Check if we have valid 2nd smallest and 2nd largest
    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None
    
    return (second_smallest, second_largest)

