from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    """
    Calculates the Weighted Mean Absolute Deviation around the weighted mean of a dataset.
    """
    # Check if weights are positive and sum to 1
    total_weight = sum(w for x, w in numbers)
    if total_weight <= 0:
        return "Weights must be positive and sum to 1"
    
    # Calculate weighted mean
    weighted_mean = sum(x * w for x, w in numbers) / total_weight
    
    # Calculate weighted mean absolute deviation
    wmad = sum(w * abs(x - weighted_mean) for x, w in numbers) / total_weight
    
    return wmad
