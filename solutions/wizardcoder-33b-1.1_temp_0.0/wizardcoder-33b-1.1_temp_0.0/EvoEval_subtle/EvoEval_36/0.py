
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            if i != 8:
                count += str(i).count('8')
    return count