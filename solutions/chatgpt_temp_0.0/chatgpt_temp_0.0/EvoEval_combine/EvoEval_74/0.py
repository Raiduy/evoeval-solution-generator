def sum_exchange(lst1, lst2, x, y, z):
    if sum((num % 2 != 0 for num in lst1)) <= len(lst2):
        answer = 'YES'
    else:
        answer = 'NO'
    if x == y + z or y == x + z or z == x + y:
        answer = 'SUM ' + answer
    else:
        answer = 'NO_SUM ' + answer
    return answer