
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    sorted_lst = []
    lst.sort()  # Sort the list in ascending order

    while lst:
        sorted_lst.append(lst.pop(0))  # Add the minimum value to the sorted list
        if lst:
            sorted_lst.append(lst.pop())  # Add the maximum value to the sorted list

    return sorted_lst
