from fastapi import FastAPI

from api.handlers import books_v1


def create_app():
    app = FastAPI()

    # Routers
    app.include_router(books_v1.router)

    return app
