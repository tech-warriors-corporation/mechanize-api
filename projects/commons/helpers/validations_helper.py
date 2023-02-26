from re import match

class ValidationsHelper:
    @staticmethod
    def is_valid_password(password: str) -> bool:
        return len(password) >= 8 and \
               any(char.isupper() for char in password) and \
               any(char.islower() for char in password) and \
               any(char.isdigit() for char in password)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None
