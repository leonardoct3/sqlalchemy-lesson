"""
Exemplo básico de operações CRUD com SQLAlchemy
Este arquivo demonstra como usar os repositórios para realizar operações básicas
"""

from app.database import Base, engine, SessionLocal
from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.repositories import AuthorRepository, BookRepository

def create_tables():
    """Cria as tabelas no banco de dados"""
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

def example_crud():
    """Exemplo de operações CRUD básicas"""
    # Criar uma sessão
    session = SessionLocal()
    
    try:
        # Instanciar repositórios
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        
        # CREATE - Criar um novo autor
        print("=== CRIANDO AUTOR ===")
        new_author = AuthorModel(name="J.K. Rowling", email="jk@example.com")
        saved_author = author_repo.add(new_author)
        print(f"Autor criado: {saved_author}")
        
        # CREATE - Criar livros
        print("\n=== CRIANDO LIVROS ===")
        book1 = BookModel(title="Harry Potter e a Pedra Filosofal", isbn="9780439708180")
        book2 = BookModel(title="Harry Potter e a Câmara Secreta", isbn="9780439064873")
        
        # Add authors to books using many-to-many relationship
        book1.authors.append(saved_author)
        book2.authors.append(saved_author)
        
        saved_book1 = book_repo.add(book1)
        saved_book2 = book_repo.add(book2)
        print(f"Livro 1 criado: {saved_book1}")
        print(f"Livro 2 criado: {saved_book2}")
        
        # READ - Buscar todos os autores
        print("\n=== BUSCANDO TODOS OS AUTORES ===")
        all_authors = author_repo.get_all()
        for author in all_authors:
            print(f"Autor: {author}")
        
        # READ - Buscar autor por ID
        print("\n=== BUSCANDO AUTOR POR ID ===")
        author_by_id = author_repo.get_by_id(saved_author.id)
        print(f"Autor encontrado: {author_by_id}")
        
        # READ - Buscar livros de um autor
        print("\n=== BUSCANDO LIVROS DO AUTOR ===")
        author_books = book_repo.get_by_author_id(saved_author.id)
        for book in author_books:
            print(f"Livro: {book}")
        
        # UPDATE - Atualizar um autor
        print("\n=== ATUALIZANDO AUTOR ===")
        saved_author.email = "jkrowling@newexample.com"
        updated_author = author_repo.update(saved_author)
        print(f"Autor atualizado: {updated_author}")
        
        # READ - Buscar por email
        print("\n=== BUSCANDO POR EMAIL ===")
        author_by_email = author_repo.get_by_email("jkrowling@newexample.com")
        print(f"Autor encontrado por email: {author_by_email}")
        
        print("\n=== OPERAÇÕES CONCLUÍDAS COM SUCESSO! ===")
        
    except Exception as e:
        print(f"Erro durante as operações: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    # Criar tabelas
    create_tables()
    
    # Executar exemplos
    example_crud()

