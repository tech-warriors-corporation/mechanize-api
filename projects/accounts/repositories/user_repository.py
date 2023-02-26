from projects.commons.enums.user_role_enum import UserRoleEnum
from projects.commons.helpers.database_helper import DatabaseHelper

class UserRepository:
    def __init__(self):
        self.database_helper = DatabaseHelper()

    def create(self, name: str, email: str, password: str, role: UserRoleEnum):
        connection = self.database_helper.get_connection()
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO users (name, email, password, role) VALUES ('{name}', '{email}', '{password}', '{role}')")
        connection.commit()
        cursor.close()
