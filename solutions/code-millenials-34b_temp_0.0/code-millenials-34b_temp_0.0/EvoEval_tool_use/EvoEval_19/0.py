def is_valid_day(day: str) -> bool:
    """Check if the input string is one of the seven days of the week.
    
    Args:
        day: A string representing the name of the day.

    Returns:
        bool: True if the string is one of 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 
        case sensitive. False otherwise.
    """
    valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day.title() in valid_days:
        return True
    else:
        return False
from typing import List

def sort_days(days: str) -> str:
    """Input is a comma-delimited string of days of the week. 
    Each day is written in English and is case insensitive. 
    Valid days are 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'.

    Return the string with days sorted in the order they appear in a week starting from Monday. 
    If a day is not valid, exclude it from the result.

    >>> sort_days('Sunday, monday, friday')
    'Monday, Friday, Sunday'
    """
    valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_list = days.split(',')
    sorted_days = sorted([day.title() for day in days_list if is_valid_day(day.title())], key=valid_days.index)
    return ', '.join(sorted_days)