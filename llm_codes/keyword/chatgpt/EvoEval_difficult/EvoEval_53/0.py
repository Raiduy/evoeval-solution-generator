
def add_elements(list1: list, list2: list, index: int):
    try:
        result = list1[index] + list2[index]
        exception_occurred = False
    except IndexError:
        result = None
        exception_occurred = True

    return result, exception_occurred

# Test cases
print(add_elements([1, 2, 3], [4, 5, 6], 1))  # Output: (7, False)
print(add_elements([10, 20, 30], [40, 50], 2))  # Output: (None, True)
