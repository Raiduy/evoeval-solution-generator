
from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    weights = [x[1] for x in numbers]
    if any(w <= 0 for w in weights) or sum(weights) != 1:
        return 'Weights must be positive and sum to 1'
    
    weighted_mean = sum(x[0] * x[1] for x in numbers)
    weighted_mad = sum(x[1] * abs(x[0] - weighted_mean) for x in numbers) / sum(weights)
    
    return weighted_mad
