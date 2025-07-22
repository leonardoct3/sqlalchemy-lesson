"""
Exemplo de relacionamentos com SQLAlchemy
Este arquivo demonstra como trabalhar com relacionamentos entre entidades
"""

from app.database import Base, engine, SessionLocal
from app.models import Author, Book
from app.repositories import AuthorRepository, BookRepository

def relationships_example():
    """Exemplo de como trabalhar com relacionamentos"""
    session = SessionLocal()
    
    try:
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        
        # Criar autor
        print("=== CRIANDO AUTOR ===")
        author = Author(name="George Orwell", email="orwell@example.com")
        saved_author = author_repo.add(author)
        
        # Criar livros relacionados
        print("\n=== CRIANDO LIVROS RELACIONADOS ===")
        book1 = Book(title="1984", author_id=saved_author.id)
        book2 = Book(title="A Revolução dos Bichos", author_id=saved_author.id)
        
        book_repo.add(book1)
        book_repo.add(book2)
        
        # Buscar autor com livros (usando relacionamento)
        print("\n=== ACESSANDO RELACIONAMENTOS ===")
        author_with_books = author_repo.get_by_id(saved_author.id)
        print(f"Autor: {author_with_books.name}")
        print("Livros do autor:")
        for book in author_with_books.books:
            print(f"  - {book.title}")
        
        # Buscar livro com autor
        print("\n=== ACESSANDO AUTOR ATRAVÉS DO LIVRO ===")
        books_with_authors = book_repo.get_books_with_authors()
        for book in books_with_authors:
            print(f"Livro: {book.title} | Autor: {book.author.name}")
        
        # Buscar autores que têm livros
        print("\n=== AUTORES COM LIVROS ===")
        authors_with_books = author_repo.get_authors_with_books()
        for author in authors_with_books:
            print(f"Autor com livros: {author.name} ({len(author.books)} livros)")
        
        print("\n=== RELACIONAMENTOS DEMONSTRADOS COM SUCESSO! ===")
        
    except Exception as e:
        print(f"Erro: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    # Criar tabelas se não existirem
    Base.metadata.create_all(bind=engine)
    
    # Executar exemplo
    relationships_example()

