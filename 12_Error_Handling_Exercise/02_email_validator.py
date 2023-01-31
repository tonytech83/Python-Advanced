class NameTooShortError(Exception):
    """
    Raise custom error when the name in the email is less than or equal to 4 symbols.
    """
    pass


class MustContainAtSymbolError(Exception):
    """
    Raise custom error when there is no "@" in the email.
    """
    pass


class InvalidDomainError(Exception):
    """
    Raise custom error when the domain of the email is not in invalid_domains list.
    """
    pass


def is_domain_invalid(domain, valid_domains):
    """
    Check is the domain not valid.
    """
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            return False
    return True


valid_domains = ['.com', '.bg', '.org', '.net']

while True:
    email = input()

    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    name, domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if is_domain_invalid(domain, valid_domains):
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email is valid')