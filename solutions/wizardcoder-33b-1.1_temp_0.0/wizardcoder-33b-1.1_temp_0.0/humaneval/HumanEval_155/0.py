
def even_odd_count(num):
    num = abs(num)  # make sure the number is positive
    even_count = 0
    odd_count = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
