
def next_smallest(lst):
    if not lst or len(set(lst)) == 1:
        return None
    else:
        lst.sort()
        for i in range(1, len(lst)):
            if lst[i] != lst[0]:
                return lst[i]
        return None