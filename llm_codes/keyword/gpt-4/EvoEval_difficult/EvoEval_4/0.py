
def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    # Calculate the weighted mean
    weighted_sum = sum(x * w for x, w in numbers)
    total_weight = sum(w for _, w in numbers)

    # Check if weights are positive and sum to 1
    if total_weight <= 0 or abs(total_weight - 1) > 1e-9:
        return "Weights must be positive and sum to 1"

    weighted_mean = weighted_sum / total_weight

    # Calculate the weighted mean absolute deviation
    wmad = sum(w * abs(x - weighted_mean) for x, w in numbers) / total_weight

    return wmad
