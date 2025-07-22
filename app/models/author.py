from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', email='{self.email}')>"

