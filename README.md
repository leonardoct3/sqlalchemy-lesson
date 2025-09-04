# SQLAlchemy com Clean Architecture - Projeto Prático

Este repositório contém a implementação prática do **Handout SQLAlchemy com Clean Architecture**, servindo como material didático para estudantes que estão aprendendo a integrar SQLAlchemy com princípios de arquitetura limpa.

## 🎯 Objetivos do Projeto

- Demonstrar o uso prático do **SQLAlchemy 2.0** como ORM
- Aplicar princípios de **Clean Architecture** 
- Implementar o **padrão Repository** para abstração de dados
- Usar **Pydantic** para validação e serialização
- Gerenciar **migrações** com Alembic
- Preparar a base para futuras **APIs REST**

## 🏗️ Arquitetura do Projeto

O projeto segue os princípios da Clean Architecture, organizando o código em camadas bem definidas:

```
sqlalchemy-lesson/
├── app/
│   ├── database/          # 🗄️ Configuração do banco de dados
│   │   ├── database.py    # Engine, SessionLocal, Base
│   │   └── __init__.py
│   ├── entities/          # 🏗️ Entidades de domínio (Pydantic)
│   │   ├── author.py      # Entidade Author
│   │   └── book.py        # Entidade Book
│   ├── models/            # 📊 Modelos SQLAlchemy (ORM)
│   │   ├── author_model.py    # AuthorModel + association table
│   │   ├── book_model.py      # BookModel
│   │   └── __init__.py
│   └── repositories/      # 🔄 Padrão Repository
│       ├── base_repository.py     # Repository genérico
│       ├── author_repository.py   # Repository específico
│       └── book_repository.py     # Repository específico
├── examples/              # 📚 Exemplos de uso
│   ├── complete_example.py       # Exemplo completo
│   ├── schemas_example.py        # (para desenvolvimento futuro)
│   └── simple_entities_example.py # (para desenvolvimento futuro)
├── alembic/              # 🔄 Migrações de banco
│   ├── env.py           # Configuração do Alembic
│   └── versions/        # Arquivos de migração
├── .env                 # Variáveis de ambiente
├── .env.example         # Exemplo de configuração
├── requirements.txt     # Dependências do projeto
└── alembic.ini         # Configuração do Alembic
```

### 🔍 Explicação das Camadas

#### Database Layer (Infraestrutura)
Responsável pela configuração da conexão com o banco de dados:
- **Engine**: Gerencia conexões com o banco
- **SessionLocal**: Factory para criar sessões
- **Base**: Classe base para modelos ORM

#### Entities (Domínio)
Entidades de domínio usando **Pydantic** para:
- ✅ Validação automática de dados
- ✅ Serialização/deserialização JSON  
- ✅ Type hints nativos
- ✅ Independência de tecnologia de persistência

#### Models (Infraestrutura ORM)
Modelos SQLAlchemy que mapeiam entidades para tabelas:
- 🔗 Relacionamentos entre tabelas
- 📋 Definição de colunas e tipos
- 🔑 Chaves primárias e estrangeiras
- 📊 Índices para performance

#### Repositories (Interface de Dados)
Implementação do padrão Repository:
- 🎯 Abstração de acesso a dados
- 🔄 Operações CRUD padronizadas
- 🔍 Consultas específicas por entidade
- 🧪 Facilita testes e mocks

## 🚀 Como Usar o Projeto

### 1. Configuração Inicial

```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd sqlalchemy-lesson

# Criar e ativar ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS  
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configuração do Banco

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env conforme necessário
# Para SQLite (padrão): DATABASE_URL=sqlite:///./biblioteca.db
# Para PostgreSQL: DATABASE_URL=postgresql://user:pass@localhost/dbname
```

### 3. Executar Migrações

```bash
# Gerar migração inicial (se necessário)
alembic revision --autogenerate -m "Initial migration"

# Aplicar migrações
alembic upgrade head
```

### 4. Executar Exemplos

```bash
# Exemplo completo com todas as funcionalidades
python examples/complete_example.py
```

## 📋 Funcionalidades Implementadas

### ✅ CRUD Completo
- **Create**: Criação de autores e livros
- **Read**: Busca por ID, email, título, etc.
- **Update**: Atualização de registros
- **Delete**: Remoção de registros

### ✅ Relacionamentos
- **Many-to-Many**: Autores ↔ Livros
- **Association Table**: `author_book_association`
- **Eager Loading**: Carregamento otimizado

### ✅ Validações
- **Pydantic**: Validação automática de tipos
- **Email**: Validação de formato de email
- **String Length**: Limitação de tamanhos
- **Required Fields**: Campos obrigatórios

### ✅ Consultas Avançadas
- **Busca Parcial**: Por nome/título usando `ILIKE`
- **Joins**: Consultas com relacionamentos
- **Filtragem**: Por diferentes critérios

## 🔧 Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|------------|--------|--------|
| **SQLAlchemy** | 2.0.30 | ORM principal |
| **Pydantic** | 2.7.1 | Validação e serialização |
| **Alembic** | 1.13.1 | Migrações de banco |
| **PostgreSQL** | Driver | Banco de produção |
| **SQLite** | Built-in | Banco de desenvolvimento |
| **python-dotenv** | 1.0.1 | Variáveis de ambiente |

## 🎓 Conceitos Aplicados

### Clean Architecture
- **Separação de Responsabilidades**: Cada camada tem uma função específica
- **Independência de Frameworks**: Lógica de negócio independente do SQLAlchemy
- **Testabilidade**: Fácil de testar cada camada isoladamente

### Princípios SOLID

#### 🔹 Single Responsibility Principle (SRP)
```python
# Cada classe tem uma única responsabilidade
class AuthorRepository:  # Apenas acesso a dados de Author
class Author:           # Apenas representação da entidade
class AuthorModel:      # Apenas mapeamento ORM
```

#### 🔹 Open/Closed Principle (OCP)
```python
# BaseRepository está aberto para extensão, fechado para modificação
class AuthorRepository(BaseRepository[AuthorModel]):
    def get_by_email(self, email: str):  # Extensão sem modificação
        pass
```

#### 🔹 Dependency Inversion Principle (DIP)
```python
# Repository depende de abstração (Session), não implementação
class AuthorRepository:
    def __init__(self, session: Session):  # Depende da interface
        self.session = session
```

## 🚀 Próximos Passos

Este projeto serve como base para:

### 🌐 APIs REST com FastAPI
```python
@app.post("/authors/")
def create_author(author: Author, db: Session = Depends(get_db)):
    repo = AuthorRepository(db)
    # Usar o repository implementado
    return repo.add(author_model)
```

### 🧪 Testes Automatizados
- Unit tests para repositories
- Integration tests para banco de dados
- Mocks para isolamento de camadas

### 🏭 Funcionalidades Avançadas
- **Service Layer**: Lógica de negócio complexa
- **DTOs**: Separação entre entradas/saídas da API
- **Authentication**: Controle de acesso
- **Caching**: Otimização de performance

## 📚 Material de Estudo

### Handout Completo
Este projeto acompanha um **handout detalhado** disponível em:
- [Handout SQLAlchemy com Clean Architecture](../sqlalchemy-handout/)

### Conceitos Essenciais
1. **ORM (Object-Relational Mapping)**
2. **Clean Architecture Principles**
3. **Repository Pattern**
4. **Domain-Driven Design (DDD)**
5. **SOLID Principles**

### Documentação Oficial
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

## 🤝 Contribuindo

Este é um projeto educacional. Contribuições são bem-vindas para:
- 📝 Melhorias na documentação
- 🐛 Correções de bugs
- ✨ Novos exemplos práticos
- 🧪 Implementação de testes

## 📄 Licença

Este projeto é destinado para fins educacionais e está disponível sob licença MIT.

---

**Desenvolvido para ensino de SQLAlchemy e Clean Architecture** 🎓
