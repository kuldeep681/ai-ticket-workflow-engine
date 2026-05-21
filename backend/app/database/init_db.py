import app.models

from app.database.connection import engine

from app.database.session import Base


def init_db():

    Base.metadata.create_all(
        bind=engine
    )