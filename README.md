1️⃣ Pré-requisitos
Antes de iniciar, verifique se você tem instalados:
Python ≥ 3.11
PostgreSQL ≥ 15
Git (opcional, se for clonar do repositório)


2️⃣ Criar e ativar ambiente virtual
Abra o terminal na pasta do projeto.
Crie o ambiente virtual:
python -m venv venv


​
Ative o venv:
Windows:
.\venv\Scripts\activate

3️⃣ Instalar dependências do projeto
Com o venv ativo, instale os pacotes necessários:
pip install Django==5.2.7 psycopg2-binary==2.9.10 asgiref==3.10.0 sqlparse==0.5.3 tzdata==2025.2

💡 Observação: Se houver requirements.txt, pode instalar todas de uma vez:
pip install -r requirements.txt

6️⃣ Criar migrations e aplicar no banco
Criar migrations do projeto:
python manage.py makemigrations


​
Aplicar migrations (cria tabelas no PostgreSQL):
python manage.py migrate


​
Isso vai criar todas as tabelas do Django e do seu app.
7️⃣ Criar superusuário (admin)
Para acessar o Django Admin:
python manage.py createsuperuser


​
Siga os prompts: nome, e-mail (opcional) e senha.
8️⃣ Rodar o servidor de desenvolvimento
python manage.py runserver
