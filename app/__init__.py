"""
Application Factory для создания Flask приложения.
"""
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from app.extensions import db, migrate
from app.config import config_by_name


def create_app(config_name=None):
    """Создание и конфигурация Flask приложения."""
    app = Flask(__name__)

    # Загрузка конфигурации
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app.config.from_object(config_by_name[config_name])
    
    print(f"DATABASE_URL: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # ВАЖНО: Импорт внутри функции для избежания циклических импортов
    with app.app_context():
        # Регистрация Blueprints
        from app.routes.news_routes import news_bp
        app.register_blueprint(news_bp)
        
        # Импорт моделей для миграций
        from app.models.news import News

    # Регистрация обработчиков ошибок
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """Регистрация глобальных обработчиков ошибок."""
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Ресурс не найден.'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Внутренняя ошибка сервера.'}, 500
