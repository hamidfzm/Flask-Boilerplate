from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from raven.contrib.flask import Sentry
from flask_mail import Mail

__all__ = ('db', 'sentry', 'migrate', 'babel', 'mail')

db = SQLAlchemy()
sentry = Sentry()
migrate = Migrate(db=db)
babel = Babel()
mail = Mail()
