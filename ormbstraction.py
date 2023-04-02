from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class AbstractORM(ABC):
    """
    An abstract class for ORM abstractions
    """
    @abstractmethod
    def __init__(self, db_uri: str):
        pass

    @abstractmethod
    def create_all(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def get(self, entity_type, id_):
        pass

    @abstractmethod
    def get_all(self, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass


class SQLAlchemyORM(AbstractORM):
    """
    A SQLAlchemy ORM abstraction
    """

    def __init__(self, db_uri: str):
        engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=engine)

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def add(self, entity):
        session = self.Session()
        session.add(entity)
        session.commit()

    def get(self, entity_type, id_):
        session = self.Session()
        return session.query(entity_type).get(id_)

    def get_all(self, entity_type):
        session = self.Session()
        return session.query(entity_type).all()

    def update(self, entity):
        session = self.Session()
        session.merge(entity)
        session.commit()

    def delete(self, entity):
        session = self.Session()
        session.delete(entity)
        session.commit()
