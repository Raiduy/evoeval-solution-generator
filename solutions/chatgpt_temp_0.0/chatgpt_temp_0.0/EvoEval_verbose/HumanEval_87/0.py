
def get_row(lst, x):
    coordinates = []
    for (i, row) in enumerate(lst):
        for (j, element) in enumerate(row):
            if element == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    return coordinates