
def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = round(s * (s - a) * (s - b) * (s - c), 2)
    return area