
def next_smallest_and_largest(lst):
    if len(lst) < 2:
        return (None, None)
    
    smallest = largest = None
    smallest_count = largest_count = 0
    
    for num in lst:
        if smallest is None or num < smallest:
            smallest = num
            smallest_count = 1
        elif num == smallest:
            smallest_count += 1
        
        if largest is None or num > largest:
            largest = num
            largest_count = 1
        elif num == largest:
            largest_count += 1
    
    if smallest_count > 1 or largest_count > 1:
        return (None, None)
    
    return (smallest, largest)
