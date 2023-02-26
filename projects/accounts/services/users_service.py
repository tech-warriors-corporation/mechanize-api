from projects.accounts.repositories.user_repository import UserRepository
from projects.commons.enums.user_role_enum import UserRoleEnum
from cryptocode import encrypt
from projects.commons.helpers.validations_helper import ValidationsHelper
from os import environ

class UsersService:
    def __init__(self):
        self.repository = UserRepository()

    def create(self, name: str, email: str, password: str, role: UserRoleEnum):
        if not name:
            raise ValueError('Name is required')

        if not ValidationsHelper.is_valid_email(email):
            raise ValueError('Invalid email')

        if not ValidationsHelper.is_valid_password(password):
            raise ValueError('Password must be at least 8 characters and contain at least one uppercase letter, one lowercase letter and one digit')

        if role is not UserRoleEnum.DRIVER.value and role is not UserRoleEnum.MECHANIC.value:
            role = UserRoleEnum.DRIVER.value

        self.repository.create(name, email, encrypt(password, environ.get("CRYPTOCODE_PASSWORD")), role)
