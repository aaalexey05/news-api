"""
Схема для валидации и сериализации данных
"""
from marshmallow import Schema, fields, validates, ValidationError


class NewsSchema(Schema):
    """Схема для валидации новостей"""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(allow_none=True)
    publication_date = fields.DateTime(dump_only=True)

    @validates('title')
    def validate_title(self, value):
        if not value or not value.strip():
            raise ValidationError('УПС... Ошибка! Заголовок должен быть заполнен.')
        if len(value) > 255:
            raise ValidationError('Заголовок не может быть длинее 255 символов')

    """
    Валидация других полей не требуется, т.к content использует тип данных
    TEXT, что не ограничивается по кол-ву симоволов и может быть пустым
    Время автоматиячески добавляется, при создании записи
    id - автоматически увеличивается в БД (id += 1)
    """   
    # @validates('content')
    # def validate_content(self, value):


class NewsPaginationSchema(Schema):
    """Схема для пагинации"""
    total_items = fields.Int()
    total_pages = fields.Int()
    current_page = fields.Int()
    per_page = fields.Int()
    news = fields.List(fields.Nested(NewsSchema))