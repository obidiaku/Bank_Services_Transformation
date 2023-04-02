import pytest
from flask import json
from presentationlayer import app
from database import db


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_bookmark(client):
    data = {"title": "education", "url": "https://www.google.com",
            "notes": "Learning Center"}
    response = client.post('/bookmarks', json=data)
    assert response.status_code == 200
    assert response.json == {"id": 1}


def test_get_bookmarks(client):
    response = client.get('/bookmarks')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_bookmark(client):
    response = client.get('/bookmarks/1')
    assert response.status_code == 200
    assert response.json['title'] == "education"
    assert response.json['url'] == "https://www.google.com"
    assert response.json['notes'] == "Learning Center"


def test_update_bookmark(client):
    data = {"title": "education", "url": "https://www.google.com",
            "notes": "Learning Center (updated)"}
    response = client.put('/bookmarks/1', json=data)
    assert response.status_code == 204


def test_delete_bookmark(client):
    response = client.delete('/bookmarks/1')
    assert response.status_code == 204
