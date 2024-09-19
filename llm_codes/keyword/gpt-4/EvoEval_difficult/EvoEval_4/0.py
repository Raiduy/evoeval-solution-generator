
def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    # Calculate the weighted mean
    total_weight = sum(w for x, w in numbers)
    if total_weight <= 0:
        return "Weights must be positive and sum to 1"
    weighted_mean = sum(x * w for x, w in numbers) / total_weight

    # Calculate the weighted mean absolute deviation
    wmad = sum(w * abs(x - weighted_mean) for x, w in numbers) / total_weight

    return wmad
