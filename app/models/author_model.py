from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

# Many-to-many association table for authors and books
author_book_association = Table(
    'author_book_association',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
)

class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Many-to-many relationship with books
    books = relationship("BookModel", secondary=author_book_association, back_populates="authors")

    def __repr__(self):
        return f"<AuthorModel(id={self.id}, name='{self.name}', email='{self.email}')>"

