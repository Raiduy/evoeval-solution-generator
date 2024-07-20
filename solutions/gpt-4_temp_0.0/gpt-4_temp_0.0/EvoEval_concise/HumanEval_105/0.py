
def by_length(arr):
    """
    This function takes an array of integers and performs a series of operations. It first filters out numbers 
    that are not between 1 and 9 inclusive. Then, it sorts the resulting array in ascending order, reverses it, 
    and replaces each digit with its corresponding English word 
    ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine").

    Example:
      For input array [2, 1, 1, 4, 5, 8, 2, 3], the function returns ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"].
      For an empty array, it returns an empty array.
      For an array with integers outside the 1-9 range, such as [1, -1 , 55], the function ignores those numbers and returns ['One'].
    """
    arr = list(filter(lambda x: 1 <= x <= 9, arr))
    arr.sort(reverse=True)
    digit_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    arr = [digit_to_word[i] for i in arr]
    return arr