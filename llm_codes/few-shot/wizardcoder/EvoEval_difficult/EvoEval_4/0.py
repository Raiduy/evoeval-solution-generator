
from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    # Check if weights sum to 1
    if sum(w for _, w in numbers) != 1:
        return "Weights must be positive and sum to 1"

    # Calculate the weighted mean
    weighted_mean = sum(x * w for x, w in numbers)

    # Calculate the Weighted Mean Absolute Deviation
    weighted_mean_abs_deviation = sum(w * abs(x - weighted_mean) for x, w in numbers) / sum(w for _, w in numbers)

    return weighted_mean_abs_deviation
