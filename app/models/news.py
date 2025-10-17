"""
Модель данных для новостей
"""

from datetime import datetime
from app.extensions import db


class News(db.Model):
    """Модель новостей"""
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    publication_date = db.Column(
        db.DateTime,
        nullable = False,
        default = datetime.utcnow
    )

    def __repr__(self):
        return f"<News {self.id}: {self.title[:30]}>"
    
    def to_dict(self):
        """Сериализация модели в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "publication_date": self.publication_date
        }  # Возвращаем словарь с данными: id, title(not null), content(null), publication_date