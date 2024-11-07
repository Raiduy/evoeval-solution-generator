def next_smallest_and_largest(lst):
    first_min = float('inf')
    second_min = float('inf')
    first_max = float('-inf')
    second_max = float('-inf')

    for num in lst:
        if num < first_min:
            first_min, second_min = num, first_min
        elif first_min < num < second_min:
            second_min = num

        if num > first_max:
            first_max, second_max = num, first_max
        elif first_max > num > second_max:
            second_max = num

    return (second_min, second_max) if second_min != float('inf') and second_max != float('-inf') else (None, None)