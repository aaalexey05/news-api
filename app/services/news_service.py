"""
Бизнес-логика для работы с новостями
"""
from app.models.news import News
from app.extensions import db


class NewsService:
    """Сервис для управления новостями (аналогично можно добавить другие сервисы)"""

    @staticmethod
    def get_all_news(page=1, per_page=10):
        """
        Получаем все новости в форме списка + пагинация
        
        Args<
        page: номер страницы
        per_page: количество элементов на странице
        >

        Returns <dict: словарь с новостями и метаинформацией>
        """
        paginated = News.query.order_by(
            News.publication_date.desc()
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return {
            "total_items": paginated.total,
            "total_pages": paginated.pages,
            "current_page": paginated.page,
            "per_page": paginated.per_page,
            "news": [news.to_dict() for news in paginated.items]
        }
    
    @staticmethod
    def get_news_by_id(news_id):
        """
        Получаем новости по ID
        news_id: ID новости
        News: объект новости или значение None
        """

        return News.query.get(news_id)
    
    @staticmethod
    def create_news(data):
        """
        Создание новости
        data: словарь с данными новости
        News: созданный объект новости
        """
        
        news = News(
            title=data['title'],
            content=data.get('content')
        )

        db.session.add(news)
        db.session.commit()

        return news
    
    @staticmethod
    def update_news(news_id, data):
        """
        Обновление новости (существующей)
        news_id: ID новости
        data: словарь с новыми данными
        News: обновленный объект новости или None
        """
        news = News.query.get(news_id)

        if not news:
            return None
        
        news.title = data['title']
        news.content = data.get('content', news.content)
        db.session.commit()
        
        return news
    
    @staticmethod
    def delete_news(news_id):
        """
        Удалить новость
        news_id: ID новости
        bool: True, если удалено и False, если не найдена запись
        """
        news = News.query.get(news_id)

        if not news:
            return False
        
        db.session.delete(news)
        db.session.commit()
        
        return True
