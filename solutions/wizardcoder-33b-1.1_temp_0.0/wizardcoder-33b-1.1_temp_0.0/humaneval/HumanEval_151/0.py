
def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and i >= 0 and isinstance(i, int))
