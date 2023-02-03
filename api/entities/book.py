from typing import Set, Optional

from api.entities.sheet import Sheet


class Book:
    def __init__(
        self,
        *,
        book_id: str,
        owner: str,
        editors: Set[str] | None = None,
        readers: Set[str] | None = None,
        sheets: Set[Sheet] | None = None,
    ):
        if book_id is None:
            raise ValueError("Movie ID is required")
        self._id = book_id
        self._owner = owner
        self._editors = editors
        self._readers = readers
        self._sheets = sheets

    @property
    def id(self) -> str:
        return self._id

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def editors(self) -> Set[str] | None:
        return self._editors

    @property
    def readers(self) -> Set[str] | None:
        return self.readers

    @property
    def sheets(self) -> Set[Sheet] | None:
        return self._sheets
