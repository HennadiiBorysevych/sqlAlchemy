from sqlalchemy import text, insert
from database import engine, async_engine
from models import metadata, users

def create_all():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def insert_date():
    with engine.connect() as conn:
        info = insert(users).values(
            [
                {"name":'artem'},
                {"name": 'gena'}
            ]
        )
        conn.execute(info)
        conn.commit()