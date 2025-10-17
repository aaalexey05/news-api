"""
Конфигурация для получения информации из переменной окружения (.env)
"""
import os # можно использовать python-dotenv
from datetime import timedelta


class Config:
    """Основная конфигурация"""
    SECRET_KEY = os.environ.get("SECRET_KEY", 'input-your-secretKey-here') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = True  # поддержка кирилицы в JSON-объектах


class DevelopmentConfig(Config):
    """Конфигурация для разработки"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        'postgresql://username:password@localhost:5432/db-name'
    )


class TestingConfig(Config):
    """Конфигурация для тестирования"""
    TESTING = True
    SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'  # чтобы не трогать нашу базу данных, при тестировании будет создана база данных SQLite (временно)


class ProductionConfig(Config):
    """Конфигурация для продакшена"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}