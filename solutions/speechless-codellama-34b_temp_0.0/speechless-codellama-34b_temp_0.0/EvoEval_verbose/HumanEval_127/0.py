
def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = end - start + 1
    if length < 2:
        return 'NO'
    for i in range(2, length):
        if length % i == 0:
            return 'NO'
    return 'YES'