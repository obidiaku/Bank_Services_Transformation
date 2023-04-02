# flask API presentation layer

from flask import Flask, jsonify, request
from serviceslayer import add_bookmark, get_bookmarks, get_bookmark, update_bookmark, delete_bookmark
from database import DatabaseManager

app = Flask(__name__)

# Initialize database manager
db_manager = DatabaseManager('database.db')
#db_manager = DatabaseManager()

# Define endpoints


@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    # Retrieve bookmarks from database
    bookmarks = db_manager.select('bookmarks')
    # Convert bookmarks to list of dictionaries
    bookmarks_list = [
        {'id': row[0], 'title': row[1], 'url': row[2],
            'notes': row[3], 'date_added': row[4]}
        for row in bookmarks
    ]
    # Return bookmarks as JSON
    return jsonify(bookmarks_list)


@app.route('/bookmarks', methods=['POST'])
def add_bookmark():
    # Parse request data
    data = request.get_json()
    # Insert new bookmark into database
    db_manager.add('bookmarks', data)
    # Return success message
    return jsonify({'message': 'Bookmark added successfully'})


@app.route('/bookmarks/<int:bookmark_id>', methods=['DELETE'])
def delete_bookmark(bookmark_id):
    # Delete bookmark from database
    db_manager.delete('bookmarks', {'id': bookmark_id})
    # Return success message
    return jsonify({'message': 'Bookmark deleted successfully'})


@app.route('/all_bookmarks', methods=['GET'])
def get_all_bookmarks():
    bookmarks_list = get_bookmarks()
    return jsonify(bookmarks_list)


if __name__ == '__main__':
    app.run(debug=True)
