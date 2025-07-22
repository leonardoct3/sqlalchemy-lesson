from sqlalchemy.orm import Session
from app.models.author import Author
from app.repositories.base_repository import BaseRepository

class AuthorRepository(BaseRepository[Author]):
    def __init__(self, session: Session):
        super().__init__(session, Author)

    def get_by_email(self, email: str) -> Author | None:
        """Busca um autor pelo email"""
        return self.session.query(Author).filter(Author.email == email).first()

    def get_by_name(self, name: str) -> list[Author]:
        """Busca autores pelo nome (busca parcial)"""
        return self.session.query(Author).filter(Author.name.ilike(f"%{name}%")).all()

    def get_authors_with_books(self) -> list[Author]:
        """Retorna autores que têm livros"""
        return self.session.query(Author).join(Author.books).distinct().all()

