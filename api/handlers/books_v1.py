from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/books")


@router.get("/get_book_by_id")
async def get_book_by_id():
    pass
