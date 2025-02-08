from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = 'Books'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    description: Mapped[str]
    comment_id: Mapped[int] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(nullable=False)


class Comment(Base):
    __tablename__ = 'Comments'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False) 
    text: Mapped[str]


class Category(Base):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
