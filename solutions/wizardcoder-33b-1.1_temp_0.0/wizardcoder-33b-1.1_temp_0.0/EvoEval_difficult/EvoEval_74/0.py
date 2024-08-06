def total_match(lst1, lst2, k):
    total_chars_lst1 = sum((len(s) for s in lst1))
    total_chars_lst2 = sum((len(s) for s in lst2))
    count_lst1 = sum((1 for s in lst1 if len(s) <= k))
    count_lst2 = sum((1 for s in lst2 if len(s) <= k))
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    elif count_lst1 > count_lst2:
        return lst1
    elif count_lst1 < count_lst2:
        return lst2
    else:
        return lst1