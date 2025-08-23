# API de Gerenciamento de Colaboradores Terceirizados

## Descrição do Projeto

Esta é uma API RESTful desenvolvida como projeto para a disciplina de **Técnicas de Programação**. A aplicação gerencia dados de empresas, contratos e colaboradores terceirizados, com base em um conjunto de dados públicos.

O projeto implementa uma arquitetura de API moderna utilizando FastAPI, com um banco de dados relacional, autenticação de usuários baseada em tokens JWT e autorização por perfil de usuário (comum vs. administrador).

## Funcionalidades Principais

-   **Autenticação JWT:** Sistema de login seguro com geração de tokens Bearer.
-   **Controle de Acesso por Perfil:** Rotas diferenciadas para usuários comuns (apenas leitura) e administradores (leitura e escrita).
-   **CRUD Completo:** Operações de Criar, Ler, Atualizar e Deletar para as seguintes entidades:
    -   Empresas (`Company`)
    -   Contratos (`Contract`)
    -   Funcionários (`Employee`)
    -   Usuários (`User`)
-   **Paginação:** As rotas de listagem (`GET /`) suportam paginação para lidar com grandes volumes de dados.
-   **Documentação Automática:** A API gera documentação interativa automaticamente (Swagger UI e ReDoc).

## Tecnologias Utilizadas

-   **Backend:** Python 3.12+
-   **Framework da API:** FastAPI
-   **Banco de Dados:** SQLite
-   **ORM:** SQLAlchemy
-   **Validação de Dados:** Pydantic
-   **Autenticação:** python-jose, passlib, bcrypt
-   **Servidor ASGI:** Uvicorn
-   **Manipulação de Dados (Script):** Pandas

## Configuração do Ambiente e Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO_AQUI>
cd <NOME_DA_PASTA_DO_PROJETO>
```

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual (Windows PowerShell)
.venv\Scripts\Activate.ps1

# (Para outros sistemas, como Git Bash no Windows ou Linux/macOS)
# source .venv/bin/activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias a partir do arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto, copiando o modelo do `.env.example`.

**Arquivo `.env.example`:**
```env
# Chave secreta para a codificação dos tokens JWT.
# Use um valor longo e aleatório para segurança.
SECRET_KEY=sua_chave_secreta_aqui 
```

Crie o seu arquivo `.env` e adicione sua chave.

### 5. Popular o Banco de Dados

Execute o script `populate_db.py` para criar o banco de dados `database.db` e preenchê-lo com os dados dos arquivos CSV.

*Certifique-se de que a pasta `data_csv/` com os arquivos CSV está presente na raiz do projeto.*

```bash
python populate_db.py
```

## Executando a Aplicação

Com o ambiente configurado e o banco de dados populado, inicie o servidor da API com o Uvicorn.

```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`.

## Acessando a API e a Documentação

-   **Documentação Interativa (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **Documentação Alternativa (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Na documentação interativa, você pode testar todos os endpoints. Lembre-se de usar a rota `/auth/login` primeiro para obter um token de acesso e autorizar suas requisições no botão "Authorize".