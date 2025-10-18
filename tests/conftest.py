import pytest
from app import create_app
from app.extensions import db as _db


@pytest.fixture
def app():
    """Создание и конфигурация приложения для тестов"""
    app = create_app('testing')
    
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    """Тестовый клиент для отправки запросов к приложению"""
    return app.test_client()