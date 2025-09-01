from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)  # Added ISBN for better book identification
    
    # Many-to-many relationship with authors
    authors = relationship("AuthorModel", secondary="author_book_association", back_populates="books")

    def __repr__(self):
        return f"<BookModel(id={self.id}, title='{self.title}', isbn='{self.isbn}')>"

