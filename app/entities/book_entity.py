from dataclasses import dataclass
from typing import Optional

@dataclass
class BookEntity:
    """
    Entidade de domínio para Livro
    Representa um livro no domínio da aplicação, independente da persistência
    """
    id: Optional[int] = None
    title: str = ""
    author: Optional['AuthorEntity'] = None

    def __str__(self):
        author_name = self.author.name if self.author else "Autor desconhecido"
        return f"Book: {self.title} by {author_name}"

