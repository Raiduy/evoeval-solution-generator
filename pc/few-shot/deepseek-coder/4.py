

from typing import List, Tuple

def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    """
    Calculate the Weighted Mean Absolute Deviation around the weighted mean of the dataset.
    
    Ensure that the weights are positive and that they sum to 1. Return "Weights must be positive and sum to 1" if these conditions are not met.
    
    >>> weighted_mean_absolute_deviation([(1.0, 0.1), (2.0, 0.2), (3.0, 0.3), (4.0, 0.4)])
    0.8
    """
    # Check if weights are positive and sum to 1
    total_weight = sum(weight for _, weight in numbers)
    if total_weight != 1 or any(weight <= 0 for _, weight in numbers):
        return "Weights must be positive and sum to 1"
    
    # Calculate the weighted mean
    weighted_mean = sum(x * weight for x, weight in numbers)
    
    # Calculate the Weighted Mean Absolute Deviation
    wmad = sum(weight * abs(x - weighted_mean) for x, weight in numbers)
    
    return wmad



if __name__ == '__main__':
    inputs = [[[(1.0, 0.1), (2.0, 0.2), (3.0, 0.3), (4.0, 0.4)]], [[(3.6, 0.2), (7.4, 0.3), (2.1, 0.1), (8.2, 0.15), (6.3, 0.25)]], [[(1.7, 0.15), (3.0, 0.25), (4.5, 0.35), (2.8, 0.1), (3.9, 0.15)]], [[(5.0, 0.1), (10.0, 0.2), (15.0, 0.3), (20.0, 0.4)]], [[(1.1, 0.1), (2.2, 0.2), (3.3, 0.3), (4.4, 0.4)]], [[(2.0, 0.1), (4.0, 0.2), (6.0, 0.3), (8.0, 0.4)]], [[(1.5, 0.1), (2.5, 0.2), (3.5, 0.3), (4.5, 0.4)]], [[(2.5, 0.1), (5.0, 0.2), (7.5, 0.3), (10.0, 0.4)]], [[(1.2, 0.1), (2.4, 0.2), (3.6, 0.3), (4.8, 0.4)]], [[(2.7, 0.1), (3.6, 0.2), (1.8, 0.3), (4.2, 0.4)]], [[(7.1, 0.15), (2.3, 0.25), (9.6, 0.35), (5.2, 0.25)]], [[(1.9, 0.05), (2.8, 0.15), (3.7, 0.25), (4.6, 0.35), (5.5, 0.2)]], [[(8.1, 0.1), (7.2, 0.2), (6.3, 0.3), (5.4, 0.4)]], [[(2.6, 0.1), (3.9, 0.05), (1.2, 0.35), (4.8, 0.5)]], [[(1.0, 0.25), (2.0, 0.25), (3.0, 0.25), (4.0, 0.25)]], [[(1.0, 0.1), (2.0, 0.1), (3.0, 0.1), (4.0, 0.7)]], [[(1.0, 0.25), (2.0, 0.25), (3.0, 0.25), (4.0, 0.25)]], [[(1.0, 0.1), (1.0, 0.2), (1.0, 0.3), (1.0, 0.4)]], [[(1000000000.0, 0.1), (2000000000.0, 0.2), (3000000000.0, 0.3), (4000000000.0, 0.4)]], [[(1.0, 1.0)]]]
    number_of_executions = 10461720
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = weighted_mean_absolute_deviation(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1

