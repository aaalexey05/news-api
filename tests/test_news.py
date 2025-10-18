import json


def test_create_news(client):
    response = client.post(
        '/api/news', 
        data = json.dumps({'title': 'Test', 'content': 'Content'}),
        content_type = 'application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test'


def test_get_news(client):
    response = client.get('/api/news')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'news' in data


def test_get_news_by_id_not_found(client):
    response = client.get('/api/news/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data