"""
Flask расширение, чтобы предотвратить циклические импорты.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()