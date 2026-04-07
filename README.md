<h1 align="center">
  📊 API de Gestão e Inteligência de Terceirizados (HUOL)
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/JWT-Black?style=flat&logo=JSON%20web%20tokens" alt="JWT">
</p>

## 💡 Sobre o Projeto

Esta API RESTful foi desenvolvida com o objetivo de promover **transparência e gestão eficiente de dados públicos**. Utilizando um conjunto de dados reais do Hospital Universitário Onofre Lopes (HUOL), a aplicação processa, estrutura e disponibiliza informações cruciais sobre empresas terceirizadas, contratos e distribuição de colaboradores.

Embora tenha nascido como um projeto acadêmico de Técnicas de Programação, a arquitetura foi desenhada simulando um ambiente de produção moderno, focando em segurança (autenticação JWT e controle de acesso) e performance no consumo de dados.

## 🚀 Funcionalidades Principais

- **Segurança e Auditoria:** Sistema de autenticação JWT (`Bearer tokens`) com controle de acesso rigoroso. Usuários comuns possuem acesso de leitura (transparência), enquanto administradores gerenciam a base (CRUD).
- **Gestão de Entidades (CRUD Completo):**
  - 🏢 `Company`: Gestão das empresas prestadoras de serviço.
  - 📄 `Contract`: Controle de vigência e detalhes contratuais.
  - 👥 `Employee`: Alocação de colaboradores por setor e cargo.
- **Otimização de Dados:** Paginação nativa nas rotas de listagem para garantir baixo tempo de resposta mesmo com grandes volumes de dados.
- **Documentação Viva:** Contratos da API gerados e atualizados automaticamente via Swagger UI e ReDoc.

## 🏗️ Estrutura do Projeto

O código foi organizado visando escalabilidade e separação de responsabilidades (Clean Code):

```text
📦 Terceirizados-HUOL
 ┣ 📂 models/       # Modelagens do banco de dados (SQLAlchemy)
 ┣ 📂 schemas/      # Validações e serialização de dados (Pydantic)
 ┣ 📂 routers/      # Divisão lógica dos endpoints da API
 ┣ 📂 data_csv/     # Base de dados bruta (Data Source)
 ┣ 📜 main.py       # Ponto de entrada da aplicação (FastAPI)
 ┣ 📜 populate_db.py# Pipeline de ingestão inicial (Pandas)
 ┗ 📜 requirements.txt
