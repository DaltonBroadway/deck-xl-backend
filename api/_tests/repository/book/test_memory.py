import pytest

from api.entities.book import Book
from repository.book.memory import MemoryBookRepository


@pytest.mark.asyncio
async def test_create_book():
    repo = MemoryBookRepository()
    book = Book(
        book_id="test",
        owner="test_user"
    )
    await repo.create_book(book=book)
    assert await repo.get_by_id("test") is book

