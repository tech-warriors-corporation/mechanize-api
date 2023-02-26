from psycopg2 import connect
from os import environ

_connection = None

class DatabaseHelper:
    def __init__(self):
        global _connection

        if not _connection:
            _connection = connect(
                dbname=environ.get("DB_NAME"),
                user=environ.get("DB_USER"),
                password=environ.get("DB_PASSWORD"),
                host=environ.get("DB_HOST"),
                port=environ.get("DB_PORT")
            )

        self.connection = _connection
