from typing import List, Optional

from api.entities.book import Book
from api.entities.sheet import Sheet
from repository.book.abstactions import BookRepository, BookRepositoryException


class MemoryBookRepository(BookRepository):
    """
    Implements the BookRepository pattern using a simple in-memory database
    """
    def __init__(self):
        self._storage = {}

    async def create_book(self, book: Book):
        self._storage[book.id] = book

    async def get_by_id(self, book_id: str) -> Optional[Book]:
        return self._storage.get(book_id, None)

    async def get_books_for_user(self, user_id: str) -> Optional[List[Book]]:
        return_value = []
        for _, book in self._storage.items():
            if user_id in set([book.owner] + book.editors + book.readers):
                return_value.append(book)
        return return_value

    async def update_book_owner(self, book_id: str, user_id: str):
        book = self._storage.get(book_id, None)
        if book is not None:
            book.owner = user_id

    async def add_editors_to_book(self, book_id: str, user_ids: List[str]):
        book = self._storage.get(book_id, None)
        if book is not None:
            book.editors += set(user_ids)

    async def remove_editors_from_book(self, book_id: str, user_ids: List[str]):
        book = self._storage.get(book_id, None)
        if book is not None:
            book.editors -= set(user_ids)

    async def add_readers_to_book(self, book_id: str, user_ids: List[str]):
        book = self._storage.get(book_id, None)
        if book is not None:
            book.readers += set(user_ids)

    async def remove_readers_from_book(self, book_id: str, user_ids: List[str]):
        book = self._storage.get(book_id, None)
        if book is not None:
            book.readers -= set(user_ids)

    async def add_sheet_to_book(self, sheet: Sheet, book_id: str):
        book = self._storage.get(book_id, None)
        if book is not None:
            if sheet not in book.sheets:
                raise BookRepositoryException(f"Sheet with name: {sheet.name} already exists in this book.")
            if sheet.seq == -1:
                sheet.seq = len(book.sheets)
            else:
                for s in book.sheets:
                    if sheet.seq >= s.seq:
                        s.seq += 1
            book.sheets.add(sheet)

    async def delete_sheet_from_book(self, sheet_id: str, book_id: str):
        book = self._storage.get(book_id, None)
        if book is not None:
            for sheet in book.sheets:
                if sheet.id == sheet_id:
                    book.sheets.pop(sheet)
