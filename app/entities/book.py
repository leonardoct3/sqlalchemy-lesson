from pydantic import BaseModel, Field
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .author import Author

class Book(BaseModel):
    """
    Pydantic entity for Book domain object
    Represents a book in the application domain, independent of persistence
    """
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=500, description="Book title")
    isbn: Optional[str] = Field(None, min_length=10, max_length=17, description="Book ISBN")
    authors: List['Author'] = Field(default_factory=list, description="List of book authors")

    class Config:
        # Allow ORM mode for SQLAlchemy integration
        from_attributes = True
        # JSON schema extra information
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Harry Potter and the Philosopher's Stone",
                "isbn": "9780747532699",
                "authors": []
            }
        }

    def add_author(self, author: 'Author') -> None:
        """Add an author to the book"""
        if author not in self.authors:
            self.authors.append(author)

    def remove_author(self, author: 'Author') -> None:
        """Remove an author from the book"""
        if author in self.authors:
            self.authors.remove(author)

    def __str__(self):
        author_names = [author.name for author in self.authors] if self.authors else ["Unknown Author"]
        return f"Book: {self.title} by {', '.join(author_names)}"

# Update forward references
from .author import Author
Book.model_rebuild()
