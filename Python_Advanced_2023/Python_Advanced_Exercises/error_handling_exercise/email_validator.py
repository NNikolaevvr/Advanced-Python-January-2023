class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass




email = input()

while email != "End":
    valid_mail = True

    if email.count('@') > 1:

        raise MoreThanOneAtSymbolError("Email should contain only one @!")

    if len(email.split("@")[0]) <= 4:

        raise NameTooShortError("Name must be more than 4 characters")

    if email.split('.')[-1] not in ['com', 'bg', 'org', 'net']:

        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")


    print("Email is valid")

    email = input()
