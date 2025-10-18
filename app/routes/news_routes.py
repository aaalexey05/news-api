"""
Эндпоинты API для работы с новостями.
"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc

from app.services.news_service import NewsService
from app.schemas.news_schema import NewsSchema, NewsPaginationSchema

news_bp = Blueprint('news', __name__, url_prefix='/api/news')

news_schema = NewsSchema()
news_list_schema = NewsPaginationSchema()


@news_bp.route('', methods=['GET'])
def get_news_list():
    """GET /api/news - Получить список всех новостей."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    try:
        result = NewsService.get_all_news(page, per_page)
        return jsonify(news_list_schema.dump(result)), 200
    except Exception as e:
        return jsonify({'error': 'Ошибка сервера при получении новостей.'}), 500


@news_bp.route('/<int:news_id>', methods=['GET'])
def get_news(news_id):
    """GET /api/news/<id> - Получить одну новость по ID."""
    news = NewsService.get_news_by_id(news_id)
    
    if not news:
        return jsonify({'error': f'Новость с ID {news_id} не найдена.'}), 404
    
    return jsonify(news_schema.dump(news)), 200


@news_bp.route('', methods=['POST'])
def create_news():
    """POST /api/news - Создать новую новость."""
    try:
        data = news_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    try:
        news = NewsService.create_news(data)
        return jsonify(news_schema.dump(news)), 201
    except exc.SQLAlchemyError:
        return jsonify({'error': 'Ошибка базы данных при создании новости.'}), 500


@news_bp.route('/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    """PUT /api/news/<id> - Обновить существующую новость."""
    try:
        data = news_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    try:
        news = NewsService.update_news(news_id, data)
        if not news:
            return jsonify({'error': f'Новость с ID {news_id} не найдена.'}), 404
        
        return jsonify(news_schema.dump(news)), 200
    except exc.SQLAlchemyError:
        return jsonify({'error': 'Ошибка базы данных при обновлении новости.'}), 500


@news_bp.route('/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    """DELETE /api/news/<id> - Удалить новость."""
    try:
        deleted = NewsService.delete_news(news_id)
        if not deleted:
            return jsonify({'error': f'Новость с ID {news_id} не найдена.'}), 404
        
        return '', 204
    except exc.SQLAlchemyError:
        return jsonify({'error': 'Ошибка базы данных при удалении новости.'}), 500
