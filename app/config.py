"""
Конфигурации для разных окружений.
"""
import os
from datetime import timedelta


class Config:
    """Базовая конфигурация."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False


class DevelopmentConfig(Config):
    """Конфигурация для разработки."""
    DEBUG = True
    # ПОДКЛЮЧЕНИЕ К POSTGRESQL
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://newsdbuser:root@localhost:5432/newsdb'


class TestingConfig(Config):
    """Конфигурация для тестирования."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Конфигурация для продакшена."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
