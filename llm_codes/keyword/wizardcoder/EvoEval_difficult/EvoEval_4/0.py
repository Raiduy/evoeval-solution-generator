from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float: # fix extra parenthesis ]
    weights = [w for _, w in numbers]
    if sum(weights) != 1 or min(weights) < 0:
        return "Weights must be positive and sum to 1"

    weighted_mean = sum(x * w for x, w in numbers) # fix x, _, w
    weighted_mean_absolute_deviation = sum(w * abs(x - weighted_mean) for x, w in numbers) / sum(weights) # fix x, _, w
    return weighted_mean_absolute_deviation
