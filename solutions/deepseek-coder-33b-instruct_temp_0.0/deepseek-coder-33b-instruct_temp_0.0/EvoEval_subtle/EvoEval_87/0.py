def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in descending order.
    Also, sort coordinates of the row by columns in ascending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(2, 0), (2, 5), (1, 0), (1, 4), (0, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda x: (x[0], x[1]))
    return coordinates[::-1]