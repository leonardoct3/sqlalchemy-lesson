from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AuthorEntity:
    """
    Entidade de domínio para Autor
    Representa um autor no domínio da aplicação, independente da persistência
    """
    id: Optional[int] = None
    name: str = ""
    email: str = ""
    books: List['BookEntity'] = None

    def __post_init__(self):
        if self.books is None:
            self.books = []

    def add_book(self, book: 'BookEntity'):
        """Adiciona um livro à lista de livros do autor"""
        if book not in self.books:
            self.books.append(book)
            book.author = self

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

