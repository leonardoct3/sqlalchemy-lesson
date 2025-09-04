from pydantic import BaseModel, Field
from typing import List, Optional

class Book(BaseModel):
    """
    Entidade Book usando Pydantic
    Representa um livro no domínio da aplicação
    """
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=500)
    isbn: Optional[str] = Field(None, min_length=10, max_length=17)
    authors: List['Author'] = Field(default_factory=list)

    class Config:
        # Permite conversão de objetos SQLAlchemy
        from_attributes = True

    def __str__(self):
        return f"Book: {self.title} {self.isbn}"

# Resolve forward references
from .author import Author
Book.model_rebuild()
