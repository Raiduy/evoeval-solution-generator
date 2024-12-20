

def car_race_collision(n: int) -> int:
    """
    Calculates the total number of collisions between two groups of cars moving in opposite directions.
    """
    return n * (n - 1) // 2