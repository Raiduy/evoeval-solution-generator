
    total_weight = sum(weight for _, weight in numbers)
    if total_weight <= 0:
        return "Weights must be positive and sum to 1"
    weighted_mean = sum(x * w for x, w in numbers) / total_weight
    return sum(w * abs(x - weighted_mean) for x, w in numbers) / total_weight
