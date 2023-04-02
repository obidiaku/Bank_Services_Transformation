import json
import pytest
from flask import Flask
from serviceslayer import app, add_bookmark, get_bookmarks, get_bookmark, update_bookmark, delete_bookmark

app = Flask(__name__)  #
test_client = app.test_client()


@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_bookmarks(test_client):
    response = test_client.get('/bookmarks')
    assert response.status_code == 200
    bookmarks = json.loads(response.data.decode('utf-8'))
    assert isinstance(bookmarks, list)


def test_add_bookmark(test_client):
    data = {'title': 'Test Bookmark', 'url': 'https://www.google.com'}
    response = test_client.post('/bookmarks', json=data)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')
                      ) == {'message': 'Bookmark added successfully'}


def test_delete_bookmark(test_client):
    data = {'title': 'Test Bookmark', 'url': 'https://www.google.com'}
    response = test_client.post('/bookmarks', json=data)
    bookmark_id = json.loads(response.data.decode('utf-8'))['id']
    response = test_client.delete(f'/bookmarks/{bookmark_id}')
    print(response.data)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')
                      ) == {'message': 'Bookmark deleted successfully'}


def test_get_bookmarks_returns_200(test_client):
    response = test_client.get('/bookmarks')
    assert response.status_code == 200
    assert isinstance(response.json, list)
