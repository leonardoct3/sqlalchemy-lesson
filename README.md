# Aula de Introdução ao SQLAlchemy e SQL para Iniciantes

Este repositório foi criado para servir como material didático para estudantes que estão começando a aprender SQL e desejam integrar seus conhecimentos com o SQLAlchemy, um ORM (Object-Relational Mapper) em Python. A estrutura do projeto foi pensada para ser simples e didática, focando nos conceitos essenciais de entidades, modelos e repositórios.

## Estrutura do Projeto

```
sqlalchemy_lesson/
├── app/
│   ├── database/             # Configuração do banco de dados (engine, sessão, base)
│   │   ├── database.py
│   │   └── __init__.py
│   ├── entities/             # Entidades de domínio (dataclasses Python)
│   │   ├── author_entity.py
│   │   ├── book_entity.py
│   │   └── __init__.py
│   ├── models/               # Modelos SQLAlchemy (mapeamento ORM)
│   │   ├── author.py
│   │   ├── book.py
│   │   └── __init__.py
│   ├── repositories/         # Implementação do padrão Repository
│   │   ├── base_repository.py
│   │   ├── author_repository.py
│   │   ├── book_repository.py
│   │   └── __init__.py
│   └── __init__.py
├── examples/                 # Exemplos de uso e scripts de demonstração
│   ├── basic_crud.py
│   └── relationships_example.py
├── .env.example              # Exemplo de arquivo de variáveis de ambiente
├── .env                      # Variáveis de ambiente (para uso local)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

### Explicação da Estrutura

*   **`app/database/`**: Contém a configuração para a conexão com o banco de dados, a criação do `engine` (motor de conexão), a `SessionLocal` (para gerenciar sessões de banco de dados) e a `Base` declarativa para os modelos ORM.
*   **`app/entities/`**: Define as entidades de domínio usando `dataclasses` do Python. Estas representam os objetos de negócio de forma agnóstica à persistência, ou seja, não dependem diretamente do SQLAlchemy. Isso é útil para manter a lógica de negócio separada da lógica de banco de dados.
*   **`app/models/`**: Contém os modelos SQLAlchemy que mapeiam as classes Python para tabelas no banco de dados. Aqui é onde definimos as colunas, tipos de dados e relacionamentos entre as tabelas.
*   **`app/repositories/`**: Implementa o padrão Repository, que abstrai a lógica de acesso a dados. Cada repositório é responsável por interagir com um modelo específico, fornecendo métodos para operações CRUD (Create, Read, Update, Delete) e outras consultas específicas.
*   **`examples/`**: Contém scripts Python que demonstram como usar os modelos e repositórios para interagir com o banco de dados. Inclui exemplos de operações CRUD básicas e como lidar com relacionamentos entre entidades.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd sqlalchemy_lesson
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados:**
    Este projeto usa SQLite por padrão para simplicidade, mas pode ser configurado para PostgreSQL ou outros bancos. O arquivo `.env.example` mostra as opções.

    Crie um arquivo `.env` na raiz do projeto (no mesmo nível de `requirements.txt`) e adicione a configuração do seu banco de dados. Para SQLite, você pode usar:
    ```
    DATABASE_URL=sqlite:///./biblioteca.db
    ```
    Isso criará um arquivo `biblioteca.db` no diretório raiz do projeto.

5.  **Execute os Exemplos:**
    Os scripts em `examples/` criarão as tabelas e demonstrarão as operações.

    *   **Exemplo de CRUD Básico:**
        ```bash
        python3 -m examples.basic_crud
        ```

    *   **Exemplo de Relacionamentos:**
        ```bash
        python3 -m examples.relationships_example
        ```

## Conceitos Básicos de SQL e SQLAlchemy

### O que é SQL?

SQL (Structured Query Language) é a linguagem padrão para gerenciar e manipular bancos de dados relacionais. Ele permite que você crie, leia, atualize e exclua dados (CRUD), defina a estrutura do banco de dados e gerencie permissões.

### O que é SQLAlchemy?

SQLAlchemy é um kit de ferramentas SQL de código aberto e um Object-Relational Mapper (ORM) para Python. Ele permite que os desenvolvedores interajam com bancos de dados usando objetos Python em vez de escrever SQL puro. Isso torna o código mais legível, reutilizável e menos propenso a erros.

### ORM (Object-Relational Mapper)

Um ORM é uma técnica de programação que mapeia objetos de um programa para tabelas em um banco de dados relacional. Ele atua como uma 


ponte entre a programação orientada a objetos e os bancos de dados relacionais, permitindo que os desenvolvedores trabalhem com dados como se fossem objetos Python.

### Entidades vs. Modelos

*   **Entidades (`app/entities/`)**: São classes Python simples (dataclasses) que representam os conceitos do seu domínio de negócio. Elas são independentes de qualquer tecnologia de persistência e focam na lógica de negócio. Por exemplo, `AuthorEntity` e `BookEntity` representam um autor e um livro, respectivamente, com seus atributos e comportamentos.

*   **Modelos (`app/models/`)**: São as classes que o SQLAlchemy usa para mapear para as tabelas do banco de dados. Eles herdam de `Base` do SQLAlchemy e contêm a definição das colunas e relacionamentos. Os modelos são a representação da sua entidade no banco de dados.

### Padrão Repository

O padrão Repository (Repositório) atua como uma camada de abstração entre a lógica de negócio e a camada de persistência de dados. Em vez de a lógica de negócio interagir diretamente com o SQLAlchemy (ou qualquer outra tecnologia de banco de dados), ela interage com o repositório. Isso traz vários benefícios:

*   **Separação de Preocupações**: A lógica de acesso a dados fica encapsulada no repositório, tornando o código mais limpo e fácil de manter.
*   **Testabilidade**: Facilita a escrita de testes unitários para a lógica de negócio, pois você pode "mockar" (simular) o repositório.
*   **Flexibilidade**: Permite trocar a tecnologia de persistência (por exemplo, de PostgreSQL para MongoDB) com menos impacto na lógica de negócio.

## Próximos Passos e Integração com FastAPI

Este projeto serve como uma base sólida para entender o SQLAlchemy e o padrão Repository. Para avançar, você pode explorar os seguintes tópicos:

*   **Migrações de Banco de Dados**: Ferramentas como Alembic são usadas para gerenciar alterações no esquema do banco de dados de forma controlada.
*   **Testes Unitários e de Integração**: Escrever testes para seus repositórios e lógica de negócio.
*   **Injeção de Dependência**: Usar frameworks como `fastapi.Depends` para gerenciar as sessões do banco de dados e os repositórios de forma eficiente.
*   **Integração com FastAPI**: O próximo passo natural é construir uma API RESTful usando FastAPI, expondo as operações CRUD definidas nos repositórios. O FastAPI é um framework web moderno e rápido para construir APIs com Python, e se integra muito bem com o SQLAlchemy.

    Um exemplo de como a integração pode ser feita:

    ```python
    # Exemplo de como um endpoint FastAPI pode usar o repositório
    from fastapi import FastAPI, Depends, HTTPException
    from sqlalchemy.orm import Session
    from app.database import SessionLocal
    from app.repositories import AuthorRepository
    from app.entities import AuthorEntity

    app = FastAPI()

    # Função para obter a sessão do banco de dados
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.post("/authors/", response_model=AuthorEntity)
    def create_author(author: AuthorEntity, db: Session = Depends(get_db)):
        repo = AuthorRepository(db)
        # Convertendo a entidade para o modelo SQLAlchemy para persistência
        new_author_model = Author(name=author.name, email=author.email)
        created_author = repo.add(new_author_model)
        # Convertendo o modelo persistido de volta para entidade para resposta
        return AuthorEntity(id=created_author.id, name=created_author.name, email=created_author.email)

    # Para rodar este exemplo (após instalar FastAPI e Uvicorn):
    # uvicorn main:app --reload
    ```

Este projeto visa fornecer uma base sólida para que os estudantes possam explorar o mundo do SQL e do SQLAlchemy de forma prática e organizada. Boa sorte nos estudos!

