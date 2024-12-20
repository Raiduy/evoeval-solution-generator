def check_format(plate):
    """checks if the plate follows the correct format "AA-NNNN-AA" where "A" represents an uppercase alphabet character and "N" represents a digit."""
    import re

    pattern = "[A-Z]{2}-\d{4}-[A-Z]{2}"
    return re.fullmatch(pattern, plate) is not None


def check_invalid_alphabets(plate):
    '''checks if the plate contains invalid alphabets "I", "O", or "Q"'''
    invalid_alphabets = ["I", "O", "Q"]
    return any(alphabet in plate for alphabet in invalid_alphabets)
def check_plates(plates):
    """
    checks if the plate follows the correct format "AA-NNNN-AA" where "A" represents an uppercase alphabet character and "N" represents a digit.
    The alphabets cannot be "I", "O", or "Q". 
    The license plates are separated by commas in the string.
    """
    invalid_plates = []
    plates_list = plates.split(',')
    for plate in plates_list:
        if not check_format(plate) or check_invalid_alphabets(plate):
            invalid_plates.append(plate)
    return invalid_plates