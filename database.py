
import sqlalchemy as db
import sqlite3
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy

# Define the database schema using SQLAlchemy, creating a base and defining the class
Base = declarative_base()
db = SQLAlchemy()


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))


def create_database():
    engine = db.create_engine('sqlite:///bookmarks.db')
    connection = engine.connect()
    Base.metadata.create_all(engine)
    return connection

# creating an instance of the database


class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
