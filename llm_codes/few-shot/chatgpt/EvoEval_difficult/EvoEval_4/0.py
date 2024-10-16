
from typing import List, Tuple


def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    """
    Calculate the Weighted Mean Absolute Deviation around the weighted mean of the dataset.
    """
    # Check if weights are positive and sum to 1
    if any(w <= 0 for _, w in numbers) or sum(w for _, w in numbers) != 1:
        return "Weights must be positive and sum to 1"

    # Calculate weighted mean
    weighted_mean = sum(x * w for x, w in numbers)

    # Calculate weighted mean absolute deviation
    wmad = sum(w * abs(x - weighted_mean) for x, w in numbers) / sum(w for _, w in numbers)

    return wmad
