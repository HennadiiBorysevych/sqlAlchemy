from sqlalchemy import text, insert
from database import Base, engine, async_engine, session
from models import User

def create_all():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# def insert_date():
#     with engine.connect() as conn:
#         info = insert(users).values(
#             [
#                 {"name":'artem'},
#                 {"name": 'gena'}
#             ]
#         )
#         conn.execute(info)
#         conn.commit()

def insert_date():
    user = User(name='artem')
    with session as session:
        session.add(user)
        session.commit()