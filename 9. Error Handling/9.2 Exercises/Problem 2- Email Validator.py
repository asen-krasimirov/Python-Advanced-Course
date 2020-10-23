# Email Validator


class Error(Exception):
    pass


class NameTooShortError(Error):
    """Email's name is too short."""
    pass


class MustContainAtSymbolError(Error):
    """The email does not contain @."""
    pass


class InvalidDomainError(Error):
    """The email has invalid domain."""
    pass


def name_is_too_short(name_length):
    if name_length > 4:
        return False
    return True


def invalid_domain(domains: str):
    valid_domains = [".com", ".bg", ".org", ".net"]

    top_level_domain = "." + domains.split(".")[-1]

    if top_level_domain not in valid_domains:
        return True
    return False


while True:  # Validates emails until "End" is entered as email or an exception is risen
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    if name_is_too_short(len(name)):
        raise NameTooShortError("Name must be more than 4 characters")

    if invalid_domain(domain):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
