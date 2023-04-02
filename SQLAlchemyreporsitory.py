
from abc import ABC, abstractmethod
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import List


# Import SQLAlchemy and define a Base object:

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


# Define your database model by subclassing Base:


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    notes = Column(String)
    date_added = Column(DateTime)


# Define repository interface by creating an abstract base class:
# Define concrete repository by subclassing AbstractRepository and implementing the methods:


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, bookmark: Bookmark) -> None:
        pass

    @abstractmethod
    def get(self, bookmark_id: int) -> Bookmark:
        pass

    @abstractmethod
    def get_all(self) -> List[Bookmark]:
        pass

    @abstractmethod
    def delete(self, bookmark_id: int) -> None:
        pass


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Bookmark]:
        return self.session.query(Bookmark).all()

    def get_by_id(self, id: int) -> Bookmark:
        return self.session.query(Bookmark).filter_by(id=id).first()

    def add(self, bookmark: Bookmark) -> None:
        self.session.add(bookmark)
        self.session.commit()

    def delete(self, bookmark: Bookmark) -> None:
        self.session.delete(bookmark)
        self.session.commit()

    def get(self, predicate) -> List[Bookmark]:
        return self.session.query(Bookmark).filter(predicate).all()


session = Session()
repository = SQLAlchemyRepository(session)
