import abc
from typing import Optional, List

from api.entities.book import Book
from api.entities.sheet import Sheet


class BookRepositoryException(Exception):
    pass


class BookRepository(abc.ABC):
    async def create_book(self, book: Book):
        """
        Inserts a new book into the repository

        Raises BookRepositoryException on failure
        """
        raise NotImplementedError

    async def get_by_id(self, book_id: str) -> Optional[Book]:
        """
        Retrieves a book by ID.

        Raises BookRepositoryException if not found
        """
        raise NotImplementedError

    async def get_books_for_user(self, user_id: str) -> Optional[List[Book]]:
        """
        Retrieves a list of books by User ID.
        """
        raise NotImplementedError

    async def update_book_owner(self, book_id: str, user_id: str):
        """
        Replaces Owner of given book with given user.
        """
        raise NotImplementedError

    async def add_editors_to_book(self, book_id: str, user_ids: List[str]):
        """
        Adds given users to editors array of given book.
        """
        raise NotImplementedError

    async def remove_editors_from_book(self, book_id: str, user_ids: List[str]):
        """
        Removes given users from editors array of given book.
        """
        raise NotImplementedError

    async def add_readers_to_book(self, book_id: str, user_ids: List[str]):
        """
        Adds given users to readers array of given book.
        """
        raise NotImplementedError

    async def remove_readers_from_book(self, book_id: str, user_ids: List[str]):
        """
        Removes given users from readers array of given book.
        """
        raise NotImplementedError

    async def add_sheet_to_book(self, sheet: Sheet, book_id: str):
        """
        Adds given sheet to sheets array of given book
        """
        raise NotImplementedError

    async def delete_sheet_from_book(self, sheet_id: str, book_id: str):
        """
        Adds given sheet to sheets array of given book
        """
        raise NotImplementedError
