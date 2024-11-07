from typing import List, Tuple

from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float: # extra ]
    weights_sum = sum(w for x, w in numbers)
    if weights_sum != 1.0:
        return "Weights must be positive and sum to 1"

    weighted_mean = sum(x * w for x, w in numbers) / weights_sum
    return sum(w * abs(x - weighted_mean) for x, w in numbers) / weights_sum
