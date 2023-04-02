from flask import Flask, request, jsonify
from database import DatabaseManager
from datetime import datetime
from typing import Dict

db = DatabaseManager("database.db")

app = Flask(__name__)


@app.route('/bookmarks', methods=['POST'])
def create_bookmark():
    data = request.json
    title = data['title']
    url = data['url']
    notes = data['notes']
    bookmark_id = add_bookmark(title, url, notes)
    return jsonify({'id': bookmark_id})


@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    bookmarks = get_bookmarks()
    return jsonify(bookmarks)


@app.route('/bookmarks/<int:bookmark_id>', methods=['GET'])
def get_bookmark(bookmark_id):
    bookmark = get_bookmark(bookmark_id)
    if bookmark is None:
        return jsonify({'error': 'Bookmark not found'}), 404
    else:
        return jsonify(bookmark)


@app.route('/bookmarks/<int:bookmark_id>', methods=['PUT'])
def update_bookmark(bookmark_id):
    data = request.json
    title = data.get('title')
    url = data.get('url')
    notes = data.get('notes')
    update_bookmark(bookmark_id, title=title, url=url, notes=notes)
    return '', 204


@app.route('/bookmarks/<int:bookmark_id>', methods=['DELETE'])
def delete_bookmark(bookmark_id):
    delete_bookmark(bookmark_id)
    return '', 204


@app.route('/bookmarks', methods=['POST'])
def add_bookmark():
    """
    Adds a bookmark to the database with the specified title, url, and notes.

    Returns the ID of the newly created bookmark.
    """
    now = datetime.now()
    data = {
        "title": request.json['title'],
        "url": request.json['url'],
        "notes": request.json.get('notes', ''),
        "date_added": now,
    }
    db.add("bookmarks", data)
    return jsonify({"id": db.lastrowid}), 201
