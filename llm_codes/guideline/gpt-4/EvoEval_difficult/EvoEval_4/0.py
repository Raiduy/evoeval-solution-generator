
from typing import List, Tuple
import numpy as np

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    # Convert the list of tuples to a numpy array for efficient computation
    numbers_array = np.array(numbers)

    # Separate the data points and weights
    data_points = numbers_array[:, 0]
    weights = numbers_array[:, 1]

    # Check if weights are positive and sum to 1
    if np.any(weights <= 0) or not np.isclose(np.sum(weights), 1):
        return "Weights must be positive and sum to 1"

    # Calculate the weighted mean
    weighted_mean = np.average(data_points, weights=weights)

    # Calculate the weighted mean absolute deviation
    wmad = np.sum(weights * np.abs(data_points - weighted_mean))

    return wmad
