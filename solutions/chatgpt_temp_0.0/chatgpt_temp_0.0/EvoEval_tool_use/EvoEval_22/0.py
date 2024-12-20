from typing import List, Any, Dict

def check_type(value: Any) -> str:
    """
    This helper function checks the type of the given value and returns a string representation of the type.
    """
    if isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, str):
        return 'str'
    else:
        return 'other'


def check_empty(value: Any) -> bool:
    """
    This helper function checks if a given iterable (like list or string) is empty and returns a boolean.
    """
    if isinstance(value, str) or isinstance(value, list):
        return len(value) == 0
    else:
        return False
from typing import List, Any, Dict

def categorize_values(values: List[Any]) -> Dict[str, List[Any]]:
    """
    Categorize a list of any python values based on their type and special attributes.

    - 'int', 'float', 'str', 'other' based on their type
    - 'empty' if an iterable (like list or string) is empty

    The result is a dictionary where the keys are categories ('int', 'float', 'str', 'other', 'empty') and the values are lists containing the corresponding values from the input list.

    >>> categorize_values(['a', 3.14, 5])
    {'str': ['a'], 'float': [3.14], 'int': [5], 'other': [], 'empty': []}

    >>> categorize_values([1, 2, 'abc', {}, []])
    {'str': ['abc'], 'float': [], 'int': [1, 2], 'other': [{}], 'empty': [[]]}
    """
    categorized_values = {'int': [], 'float': [], 'str': [], 'other': [], 'empty': []}
    for value in values:
        if check_empty(value):
            categorized_values['empty'].append(value)
        else:
            type_category = check_type(value)
            categorized_values[type_category].append(value)
    return categorized_values