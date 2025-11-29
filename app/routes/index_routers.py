"""
Маршрут для главной страницы (Фронтенд).
"""
from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    """Отдает главную страницу с HTML/JS приложением."""
    return render_template('index.html')