
from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    """
    Calculate the Weighted Mean Absolute Deviation around the weighted mean of the dataset.
    
    :param numbers: List of tuples where each tuple consists of a data point (x) and its associated weight (w).
    :return: Weighted Mean Absolute Deviation.
    """
    # Check if weights are positive and sum to 1
    total_weight = sum(weight for _, weight in numbers)
    if total_weight != 1 or any(weight <= 0 for _, weight in numbers):
        return "Weights must be positive and sum to 1"
    
    # Calculate the weighted mean
    weighted_mean = sum(x * w for x, w in numbers)
    
    # Calculate the Weighted Mean Absolute Deviation
    wmad = sum(w * abs(x - weighted_mean) for x, w in numbers)
    
    return wmad

