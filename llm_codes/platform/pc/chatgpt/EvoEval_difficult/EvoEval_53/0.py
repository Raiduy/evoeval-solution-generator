
def add_elements(list1: list, list2: list, index: int):
    try:
        result = list1[index] + list2[index]
        exception = False
    except IndexError:
        result = None
        exception = True
    return (result, exception)

