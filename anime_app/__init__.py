from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import settings

app = Flask(__name__)
app.config.from_object('settings.Config')



# Override SQLALCHEMY_DATABASE_URI to use the SSH tunnel
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{app.config["DB_USER"]}:{app.config["DB_PASSWORD"]}@{app.config["DB_HOST"]}:{app.config["DB_PORT"]}/{app.config["DB_NAME"]}'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models, views, error_handlers

