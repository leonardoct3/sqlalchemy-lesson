from sqlalchemy.orm import Session
from app.models.book import Book
from app.repositories.base_repository import BaseRepository

class BookRepository(BaseRepository[Book]):
    def __init__(self, session: Session):
        super().__init__(session, Book)

    def get_by_title(self, title: str) -> list[Book]:
        """Busca livros pelo título (busca parcial)"""
        return self.session.query(Book).filter(Book.title.ilike(f"%{title}%")).all()

    def get_by_author_id(self, author_id: int) -> list[Book]:
        """Busca livros de um autor específico"""
        return self.session.query(Book).filter(Book.author_id == author_id).all()

    def get_books_with_authors(self) -> list[Book]:
        """Retorna livros com informações do autor carregadas"""
        return self.session.query(Book).join(Book.author).all()

