def is_valid_input(lst):
    '''
    This helper function checks if the input is a list of integers.
    
    Parameters: 
    lst (list): list of integers

    Returns:
    boolean: True if the input is a list of integers, False otherwise 

    Examples: 
    is_valid_input([1, 2, 3]) ➞ True
    is_valid_input([1, '2', 3]) ➞ False
    is_valid_input([1, 2.0, 3]) ➞ False
    is_valid_input([]) ➞ False
    '''
    if not lst or type(lst) != list:
        return False
    return all(isinstance(i, int) for i in lst)
def find_max_product_sublist(lst):
    """
    Write a function that takes a list of integers as input. 
    The function should find the sublist of consecutive integers in the list that has the maximum product.
    The function should return this maximum product.
    
    If the input list is empty, the function should return None.
    If the input is not a list of integers, the function should return the string "Invalid input".

    The function does not need to return the sublist itself, just the product.
    
    Examples
    find_max_product_sublist([1,2,3]) ➞ 6
    find_max_product_sublist([-1,-2,-3]) ➞ 6
    find_max_product_sublist([-1,-2,3]) ➞ 6
    find_max_product_sublist([0, -4, -2, 3]) ➞ 24
    find_max_product_sublist([]) ➞ None
    find_max_product_sublist([3,'a',1]) ➞ "Invalid input"
    find_max_product_sublist([1.2, 3, 4]) ➞ "Invalid input"
    """
    if not lst:
        return None
    if not is_valid_input(lst):
        return 'Invalid input'
    max_product = lst[0]
    current_product = lst[0]
    for i in range(1, len(lst)):
        if lst[i - 1] * lst[i] > lst[i]:
            current_product = lst[i - 1] * lst[i]
        else:
            current_product = lst[i]
        max_product = max(max_product, current_product)
    return max_product