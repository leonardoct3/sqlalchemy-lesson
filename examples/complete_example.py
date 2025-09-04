"""
Exemplo Completo - SQLAlchemy com Clean Architecture
====================================================

Este exemplo demonstra o uso completo do sistema de biblioteca
implementado com SQLAlchemy e Clean Architecture.

Funcionalidades demonstradas:
- CRUD completo para Autores e Livros
- Relacionamentos many-to-many
- Buscas específicas
- Conversão entre Entities e Models
- Padrão Repository
"""

from app.database.database import SessionLocal, Base, engine
from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.repositories.author_repository import AuthorRepository
from app.repositories.book_repository import BookRepository
from app.entities.author import Author
from app.entities.book import Book

def demonstrate_crud_operations():
    """Demonstra operações CRUD básicas"""
    print("=== OPERAÇÕES CRUD ===")
    
    session = SessionLocal()
    
    try:
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        
        # CREATE - Criar um autor
        author_data = {
            "name": "Guimarães Rosa",
            "email": "guimaraes@literatura.com"
        }
        
        new_author = AuthorModel(**author_data)
        created_author = author_repo.add(new_author)
        print(f"✓ Autor criado: {created_author.name} (ID: {created_author.id})")
        
        # CREATE - Criar livros
        books_data = [
            {"title": "Grande Sertão: Veredas", "isbn": "978-8535902983"},
            {"title": "Sagarana", "isbn": "978-8535902990"}
        ]
        
        created_books = []
        for book_data in books_data:
            new_book = BookModel(**book_data)
            created_book = book_repo.add(new_book)
            created_books.append(created_book)
            print(f"✓ Livro criado: {created_book.title}")
        
        # Associar livros ao autor
        for book in created_books:
            book.authors.append(created_author)
        session.commit()
        print(f"✓ {len(created_books)} livros associados ao autor")
        
        # READ - Buscar autor por email
        found_author = author_repo.get_by_email("guimaraes@literatura.com")
        print(f"✓ Autor encontrado: {found_author.name}")
        print(f"  Livros: {[book.title for book in found_author.books]}")
        
        # UPDATE - Atualizar informações do autor
        found_author.name = "João Guimarães Rosa"
        updated_author = author_repo.update(found_author)
        print(f"✓ Autor atualizado: {updated_author.name}")
        
        # DELETE - Remover um livro
        book_to_delete = book_repo.get_by_isbn("978-8535902990")
        if book_to_delete:
            book_repo.delete(book_to_delete.id)
            print(f"✓ Livro removido: {book_to_delete.title}")
        
    finally:
        session.close()

def demonstrate_advanced_queries():
    """Demonstra consultas avançadas"""
    print("\n=== CONSULTAS AVANÇADAS ===")
    
    session = SessionLocal()
    
    try:
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        
        # Busca por nome parcial
        authors_with_rosa = author_repo.get_by_name("Rosa")
        print(f"✓ Autores com 'Rosa': {[a.name for a in authors_with_rosa]}")
        
        # Busca por título parcial
        books_with_grande = book_repo.get_by_title("Grande")
        print(f"✓ Livros com 'Grande': {[b.title for b in books_with_grande]}")
        
        # Autores que têm livros
        authors_with_books = author_repo.get_authors_with_books()
        print(f"✓ {len(authors_with_books)} autores têm livros publicados")
        
        # Livros com autores (eager loading)
        books_with_authors = book_repo.get_books_with_authors()
        for book in books_with_authors:
            authors_names = [author.name for author in book.authors]
            print(f"✓ '{book.title}' por: {', '.join(authors_names)}")
    
    finally:
        session.close()

def demonstrate_entity_conversion():
    """Demonstra conversão entre Models e Entities"""
    print("\n=== CONVERSÃO DE ENTIDADES ===")
    
    session = SessionLocal()
    
    try:
        author_repo = AuthorRepository(session)
        
        # Buscar autor do banco (Model)
        author_model = author_repo.get_by_email("guimaraes@literatura.com")
        
        if author_model:
            # Converter Model para Entity (Pydantic)
            author_entity = Author.model_validate(author_model)
            print(f"✓ Model → Entity: {author_entity}")
            
            # A entidade pode ser serializada para JSON
            author_json = author_entity.model_dump_json()
            print(f"✓ JSON: {author_json}")
            
            # E deserializada de volta
            author_from_json = Author.model_validate_json(author_json)
            print(f"✓ JSON → Entity: {author_from_json.name}")
            
    finally:
        session.close()

def demonstrate_data_validation():
    """Demonstra validação de dados com Pydantic"""
    print("\n=== VALIDAÇÃO DE DADOS ===")
    
    try:
        # Tentativa de criar autor com dados inválidos
        try:
            invalid_author = Author(
                name="",  # Nome vazio (inválido)
                email="email-inválido"  # Email inválido
            )
        except Exception as e:
            print(f"✗ Erro de validação capturado: {e}")
        
        # Criar autor com dados válidos
        valid_author = Author(
            name="Machado de Assis",
            email="machado@email.com"
        )
        print(f"✓ Autor válido criado: {valid_author.name}")
        
        # Validação de livro
        valid_book = Book(
            title="Dom Casmurro",
            isbn="978-8525406958"
        )
        print(f"✓ Livro válido criado: {valid_book.title}")
        
    except Exception as e:
        print(f"✗ Erro inesperado: {e}")

def demonstrate_relationship_management():
    """Demonstra gerenciamento de relacionamentos"""
    print("\n=== GERENCIAMENTO DE RELACIONAMENTOS ===")
    
    session = SessionLocal()
    
    try:
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        
        # Criar um livro colaborativo (múltiplos autores)
        book = BookModel(
            title="Literatura Brasileira Contemporânea",
            isbn="978-0000000001"
        )
        book = book_repo.add(book)
        
        # Buscar autores existentes
        existing_authors = author_repo.get_all()
        
        if len(existing_authors) >= 1:
            # Associar múltiplos autores ao livro
            for author in existing_authors[:2]:  # Primeiros 2 autores
                book.authors.append(author)
            
            session.commit()
            
            # Verificar relacionamentos
            updated_book = book_repo.get_by_id(book.id)
            print(f"✓ Livro '{updated_book.title}' tem {len(updated_book.authors)} autores")
            
            for author in updated_book.authors:
                print(f"  - {author.name}")
                print(f"    Total de livros: {len(author.books)}")
        
    finally:
        session.close()

def clean_database():
    """Limpa o banco de dados para demonstração"""
    print("=== LIMPANDO BANCO DE DADOS ===")
    
    session = SessionLocal()
    
    try:
        # Remover todos os dados para demonstração limpa
        session.query(AuthorModel).delete()
        session.query(BookModel).delete()
        session.commit()
        print("✓ Banco de dados limpo")
        
    finally:
        session.close()

def main():
    """Função principal que executa todas as demonstrações"""
    print("🚀 SQLAlchemy com Clean Architecture - Exemplo Completo")
    print("=" * 60)
    
    # Garantir que as tabelas existam
    Base.metadata.create_all(bind=engine)
    
    # Limpar dados existentes
    clean_database()
    
    # Executar demonstrações
    demonstrate_crud_operations()
    demonstrate_advanced_queries()
    demonstrate_entity_conversion()
    demonstrate_data_validation()
    demonstrate_relationship_management()
    
    print("\n🎉 Demonstração completa finalizada!")
    print("\nPróximos passos:")
    print("- Implementar testes unitários")
    print("- Adicionar camada de serviços")
    print("- Criar API REST com FastAPI")
    print("- Implementar autenticação e autorização")

if __name__ == "__main__":
    main()
