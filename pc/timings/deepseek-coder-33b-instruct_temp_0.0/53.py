
def add_elements(list1: list, list2: list, index: int):
    try:
        result = list1[index] + list2[index]
        return (result, False)
    except IndexError:
        return (None, True)

if __name__ == '__main__':
    inputs = [[[1, 2, 3], [4, 5, 6], 1], [[10, 20, 30], [40, 50], 2], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 4], [[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000], 5], [[11, 22, 33, 44, 55, 66, 77, 88, 99], [111, 222, 333, 444, 555, 666, 777, 888, 999], 8], [[], [], 0], [[1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 10], [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], 2], [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [110, 120, 130, 140, 150, 160, 170, 180, 190, 200], 9], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 0], [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 5], [[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000], 7], [[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [], 0], [[], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 0], [[41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], 15], [[101, 102, 103], [104, 105, 106], -1], [[107, 108, 109], [110, 111, 112], -2], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 5], [[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000], 6], [[1], [2], 0], [[], [1, 2, 3, 4, 5], 4], [[1, 2, 3, 4, 5], [], 2], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5], [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], 3], [[1.5, 2.5, 3.5, 4.5, 5.5], [6.5, 7.5, 8.5, 9.5, 10.5], 4], [[100, 200, 300, 400, 500, 600], [10, 20, 30, 40, 50, 60], 5], [[1.5, 2.7, 3.9, 4.1, 5.2], [6.3, 7.4, 8.5, 9.6], 3], [[100, 200, 300, 400, 500, 600], [], 0], [[], [10, 20, 30, 40, 50, 60], 0], [[100, 200, 300, 400, 500, 600], [10, 20, 30, 40, 50, 60], -1], [['a', 'b', 'c'], ['d', 'e', 'f'], 1], [[True, False, True], [False, True, False], 2], [[], [], 0], [[1], [2], 10]]
    number_of_executions = 1000000
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = add_elements(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1
