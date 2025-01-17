
def valid_date(date):
    if not date:
        return False
    match = re.match('(\\d{2})-(\\d{2})-(\\d{4})', date)
    if not match:
        return False
    (month, day, year) = map(int, match.groups())
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        if year % 4 != 0:
            if day > 28:
                return False
        elif year % 100 != 0:
            if day > 29:
                return False
        elif year % 400 != 0:
            if day > 28:
                return False
    return True