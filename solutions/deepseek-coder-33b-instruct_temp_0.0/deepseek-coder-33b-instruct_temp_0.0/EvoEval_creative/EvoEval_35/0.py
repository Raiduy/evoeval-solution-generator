def validate_email_structure(email: str):
    """ email is a string.
    return True if the email has a valid format (i.e., there is exactly one "@" character that is not the first or last character 
    and there is at least one "." character after the "@" character).

    >>> validate_email_structure("myemail@")
    False
    >>> validate_email_structure("myemail@domain")
    False
    >>> validate_email_structure("myemail@domain.com")
    True
    >>> validate_email_structure("myemail.domain.com")
    False
    >>> validate_email_structure("myemail@domain@domain.com")
    False
    """
    if email.count('@') != 1 or email[0] == '@' or email[-1] == '@':
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True