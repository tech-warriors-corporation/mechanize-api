from projects.accounts.controllers.users_controller import UsersController
from setup import app
from prefixes import users_prefix
from projects.commons.enums.http_method_enum import HttpMethodEnum

users_controller = UsersController()

@app.route(users_prefix, methods=[HttpMethodEnum.POST.value])
def create_user():
    return users_controller.create()
