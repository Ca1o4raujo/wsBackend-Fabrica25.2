📘 README.md
# Desafio Fabrica de Software -Sistema Acadêmico - CRUD + API de Universidades

Projeto em **Django** que implementa um sistema acadêmico simples com:

- CRUD de **Cursos** e **Alunos**.
- Integração com a **API pública de universidades** ([Hipolabs Universities API](https://universities.hipolabs.com/)).

---

## 🚀 Funcionalidades

- **Cursos**
  - Criar, listar, editar e deletar cursos.
  - Importar universidades da API externa.

- **Alunos**
  - Criar, listar, editar e deletar alunos.
  - Associar alunos a cursos.

- **API Externa**
  - Buscar universidades por país.

---

## ⚙️ Instalação

1. Clone o repositório:

git clone https://github.com/Ca1o4raujo/wsBackend-Fabrica25.2.git

cd faculdade


Crie e ative um ambiente virtual:

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


Aplique as migrações do banco de dados:

python manage.py migrate


Crie um superusuário (opcional):

python manage.py createsuperuser


Rode o servidor:

python manage.py runserver


# 🌐 Endpoints principais

Cursos:

/cursos/ → Listar cursos

/cursos/novo/ → Criar curso

/cursos/<id>id/editar/ → Editar curso

/cursos/<id>id/deletar/ → Deletar curso


Alunos:


/alunos/ → Listar alunos

/alunos/novo/ → Criar aluno

/alunos/<id>id/editar/ → Editar aluno

/alunos/<id>id/deletar/ → Deletar aluno

Universidades (API Externa)

/universidades → Buscar universidades por país


Django REST framework:


/api

/api/alunos

/api/cursos

# 📂 Estrutura básica

academico/  
├── models.py       # Modelos: Curso, Aluno

├── views.py        # Views CRUD + integração API externa

├── urls.py         # Rotas do sistema

├── templates/

│   └── academico/  # HTML dos CRUDs
requirements.txt
README.md

📖 Fonte da API Externa

Universidades: Hipolabs Universities API

Exemplo de busca:

https://universities.hipolabs.com/search?country=Brazil

🛠️ Tecnologias

Python 3.10+

Django 5.2.6

Django REST Framework

Requests (para consumir API externa)