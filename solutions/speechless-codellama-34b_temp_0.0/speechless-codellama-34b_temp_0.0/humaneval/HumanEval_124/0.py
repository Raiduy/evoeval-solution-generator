
def valid_date(date):
    if not date:
        return False
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and month == 2 and day > 29:
        return False
    return True
