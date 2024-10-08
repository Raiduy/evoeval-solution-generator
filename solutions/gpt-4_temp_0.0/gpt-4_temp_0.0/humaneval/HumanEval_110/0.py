
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Count the number of odd numbers in lst1
    odd_count_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count the number of even numbers in lst2
    even_count_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    
    # If the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2,
    # it is possible to exchange elements to make lst1 a list of only even numbers
    if odd_count_lst1 <= even_count_lst2:
        return "YES"
    else:
        return "NO"
