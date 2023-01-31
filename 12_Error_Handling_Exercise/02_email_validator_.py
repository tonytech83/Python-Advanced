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


class MoreThanOneAtSymbolError(Exception):
    """
    Raise custom error when there is more than one "@" symbol in the email.
    """
    pass


def checks_at_symbol(email: str):
    """
    Checks the contents of "@" symbol and whether it is contained more than once.
    """
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    elif email.count('@') > 1:
        raise MoreThanOneAtSymbolError('Email should contain single @ symbol')
    return email.split('@')


def domain_validation(domain: str):
    """
    Checks if the domain is in the list of valid domains.
    """
    valid_domains = ['.com', '.bg', '.org', '.net']

    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            break
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')


def name_validation(name: str):
    """
    Checks if the name is valid, more than four characters.
    """
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')


def main():
    """
    This function loops through the submitted emails in the console until "End" command is received.
    """
    while True:
        current_email = input()

        if current_email == 'End':
            break

        current_name, current_domain = checks_at_symbol(current_email)

        name_validation(current_name)

        domain_validation(current_domain)

        print('Email is valid')


main()
