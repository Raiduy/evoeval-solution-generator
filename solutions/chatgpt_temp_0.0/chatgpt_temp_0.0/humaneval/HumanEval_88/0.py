
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    sorted_array = array.copy()  # create a copy of the given array

    if len(sorted_array) < 2:  # if the array has less than 2 elements, return the copy as is
        return sorted_array

    if (sorted_array[0] + sorted_array[-1]) % 2 == 0:  # if the sum of the first and last elements is even
        sorted_array.sort(reverse=True)  # sort the array in descending order
    else:
        sorted_array.sort()  # sort the array in ascending order

    return sorted_array
