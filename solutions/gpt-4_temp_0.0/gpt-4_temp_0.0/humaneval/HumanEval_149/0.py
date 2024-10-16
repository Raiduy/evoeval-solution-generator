
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by length of each word, then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    
    return lst
