import datetime
from typing import Annotated
from sqlalchemy import  Table, Column, Integer, String, MetaData, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import enum
from database import Base

# metadata = MetaData()

# users = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('fullname', String),
# )

id_primary = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now,
    )]


class User(Base):
    __tablename__ = 'user'

    id: Mapped[id_primary]
    name: Mapped[str]


class Workload(enum.Enum):
    part_time = "part_time"
    full_time = "full_time"


class Resume(Base):
    __tablename__ = 'resume'

    id: Mapped[id_primary]
    title: Mapped[str]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    created_at: Mapped[created_at] 
    updated_at: Mapped[updated_at]