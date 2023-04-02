from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Bookmark:
    id: int
    title: str
    url: str
    notes: str
    date_added: str


class BookmarkRepository(ABC):
    @abstractmethod
    def add_bookmark(self, bookmark: Bookmark):
        pass

    @abstractmethod
    def get_bookmark(self, bookmark_id: int) -> Bookmark:
        pass

    @abstractmethod
    def get_all_bookmarks(self) -> list:
        pass

    @abstractmethod
    def delete_bookmark(self, bookmark_id: int):
        pass
