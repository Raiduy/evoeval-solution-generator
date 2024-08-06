
def intersection(interval1, interval2):
    # Find the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # If there is no intersection, return "NO"
    if start > end:
        return "NO"

    # Calculate the length of the intersection
    length = end - start

    # Check if the length is a prime number
    if length < 2:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"
    return "YES"