
def exchange(lst1, lst2):
    odd_count_lst1 = sum((1 for num in lst1 if num % 2 != 0))
    even_count_lst2 = sum((1 for num in lst2 if num % 2 == 0))
    if odd_count_lst1 <= even_count_lst2:
        return 'YES'
    else:
        return 'NO'