from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    weights_sum = sum(w for _, w in numbers)
    if weights_sum != 1.0:
        return "Weights must be positive and sum to 1"
    x_weighted_mean = sum(x * w for x, w in numbers) / weights_sum # fix wrong unpacking
    return sum(w * abs(x - x_weighted_mean) for x, w in numbers) / weights_sum # fix wrong unpacking
