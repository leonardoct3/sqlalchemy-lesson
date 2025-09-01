from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book

class Author(BaseModel):
    """
    Pydantic entity for Author domain object
    Represents an author in the application domain, independent of persistence
    """
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=255, description="Author's full name")
    email: EmailStr = Field(..., description="Author's email address")
    books: List['Book'] = Field(default_factory=list, description="List of books authored")

    class Config:
        # Allow ORM mode for SQLAlchemy integration
        from_attributes = True
        # JSON schema extra information
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "J.K. Rowling",
                "email": "jk.rowling@example.com",
                "books": []
            }
        }

    def add_book(self, book: 'Book') -> None:
        """Add a book to the author's collection"""
        if book not in self.books:
            self.books.append(book)

    def remove_book(self, book: 'Book') -> None:
        """Remove a book from the author's collection"""
        if book in self.books:
            self.books.remove(book)

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

# Update forward references
from .book import Book
Author.model_rebuild()
