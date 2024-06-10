# AlunIn Project

AlunIn é um portal de vagas voltado para alunos que estão em busca do primeiro emprego ou estágio. O objetivo do projeto é facilitar o acesso às oportunidades de emprego para alunos, permitindo que empresas cadastrem vagas e que alunos possam se candidatar a elas.

## Funcionalidades

- **Admin:** Gerenciar usuários e vagas.
- **Empresa:** Cadastrar vagas.
- **Aluno:** Cadastrar e compartilhar vagas de outras fontes, visualizar e aplicar para vagas.

## Estrutura das Entidades

### Usuário (User)

- ID
- Nome
- Email
- Senha
- Tipo de usuário (Admin, Aluno, Empresa)
- Data de criação

### Vaga (Job)

- ID
- Criador (ForeignKey para User)
- Título da vaga
- Descrição da vaga
- Requisitos
- Localização
- Tipo de emprego (Estágio, Junior)
- Link externo (opcional)
- Data de publicação

### Aplicação (Application)

- ID
- Vaga (ForeignKey para Job)
- Aluno (ForeignKey para User)
- Data de aplicação
- Status (Pendente, Aceito, Rejeitado)

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** Bootstrap
- **Banco de Dados:** SQLite (para desenvolvimento)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- Django 3.x
- Virtualenv (recomendado)

### Passos para Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/Gus-Nogueira/AlunIn-Project.git
    cd AlunIn-Project
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin:

    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

7. Acesse o projeto no navegador:

    ```
    http://127.0.0.1:8000
    ```

Desenvolvido por Gustavo Nogueira.
