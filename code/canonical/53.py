    try:
        result = list1[index] + list2[index]
        return (result, False)
    except IndexError:
        return (None, True)