from sqlalchemy.orm import Session
from app.models.book_model import BookModel
from app.repositories.base_repository import BaseRepository

class BookRepository(BaseRepository[BookModel]):
    def __init__(self, session: Session):
        super().__init__(session, BookModel)

    def get_by_title(self, title: str) -> list[BookModel]:
        """Busca livros pelo título (busca parcial)"""
        return self.session.query(BookModel).filter(BookModel.title.ilike(f"%{title}%")).all()

    def get_by_isbn(self, isbn: str) -> BookModel | None:
        """Busca livro pelo ISBN"""
        return self.session.query(BookModel).filter(BookModel.isbn == isbn).first()

    def get_books_with_authors(self) -> list[BookModel]:
        """Retorna livros com informações dos autores carregadas"""
        return self.session.query(BookModel).join(BookModel.authors).all()

