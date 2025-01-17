
def solution(lst):
    """
    Calculates the sum of odd numbers at even-indexed positions in a given integer list.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    sum_odd = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum_odd += lst[i]
    return sum_odd