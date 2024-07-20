
def max_fill(grid, capacity):
    import math
    '\n    Given a rectangular grid of wells, each well represented by a row and each unit of water by 1, \n    and a bucket with certain capacity, the function calculates the number of times the bucket \n    needs to be lowered to empty all the wells.\n    \n    Each well has a corresponding bucket for water extraction. The task is to find the number \n    of times the bucket has to be lowered into the wells.\n\n    Example 1:\n        Input: \n            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]\n            capacity : 1\n        Output: 6\n\n    Example 2:\n        Input: \n            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]\n            capacity : 2\n        Output: 5\n\n    Example 3:\n        Input: \n            grid : [[0,0,0], [0,0,0]]\n            capacity : 5\n        Output: 0\n\n    Constraints:\n        * Each well has the same length.\n        * 1 <= len(grid) <= 10^2\n        * 1 <= len(grid[:,1]) <= 10^2\n        * grid[i][j] are either 0 or 1.\n        * 1 <= capacity <= 10\n    '
    total_water = 0
    for row in grid:
        total_water += sum(row)
    return math.ceil(total_water / capacity)