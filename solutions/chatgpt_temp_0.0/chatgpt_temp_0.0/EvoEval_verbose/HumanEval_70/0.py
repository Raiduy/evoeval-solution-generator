
def strange_sort_list(lst):
    if not lst:
        return []
    sorted_lst = []
    while lst:
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            sorted_lst.append(max_val)
            lst.remove(max_val)
    return sorted_lst