# abstractRepository
# abstract repository for a bookmarks application using SQLAlchemy as the ORM:

from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from SQLAlchemyreporsitory import Bookmark
from typing import List


class AbstractBookmarkRepository(ABC):
    @abstractmethod
    def create(self, session: Session, bookmark: Bookmark) -> Bookmark:
        pass

    @abstractmethod
    def delete(self, session: Session, bookmark_id: int) -> None:
        pass

    @abstractmethod
    def get(self, session: Session, bookmark_id: int) -> Bookmark:
        pass

    @abstractmethod
    def get_all(self, session: Session) -> List[Bookmark]:
        pass
