import math

def max_fill(grid, capacity):
    import math

    # Calculate the total number of units of water in the grid
    total_water = sum(sum(row) for row in grid)

    # Calculate the number of times the buckets need to be lowered
    num_lowerings = math.ceil(total_water / capacity)

    return num_lowerings
