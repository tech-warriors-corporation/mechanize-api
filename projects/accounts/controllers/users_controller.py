from projects.accounts.services.users_service import UsersService
from projects.commons.helpers.response_helper import ResponseHelper
from projects.commons.enums.status_code_enum import StatusCodeEnum
from flask import request

class UsersController:
    def __init__(self):
        self.service = UsersService()

    def create(self):
        try:
            data = request.get_json()

            self.service.create(data['name'], data['email'], data['password'], data['role'])

            return ResponseHelper.generate(status_code=StatusCodeEnum.CREATED.value)
        except Exception as error:
            print(error)

            return ResponseHelper.generate(status_code=StatusCodeEnum.BAD_REQUEST.value)
