from flask import Flask
from flask_cors import CORS
from prefixes import root_prefix
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

CORS(app, resources={f"/{root_prefix}/*": { "origins": "*" }})

import projects.accounts.routes.users_routes

if __name__ == '__main__':
    app.run(debug=True, port=8000)
