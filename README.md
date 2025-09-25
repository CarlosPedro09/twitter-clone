# Twitter Clone - Projeto Final

## Descrição
Projeto final do curso, um clone simplificado do Twitter, com funcionalidades de autenticação, feed de notícias, seguidores, curtidas e comentários.

---

## **Funcionalidades**
- Sistema de cadastro e login seguro de usuários.
- Edição de perfil com avatar, nome e bio.
- Sistema de seguir e feed de notícias (apenas posts de usuários seguidos).
- Curtidas e comentários em postagens.
- Backend em Django REST Framework.
- Frontend pode ser integrado com React ou templates Django.

---

## **Tecnologias Utilizadas**
- **Backend:** Python, Django, Django REST Framework
- **Banco de Dados:** PostgreSQL
- **Frontend:** React (ou templates Django)
- **Outros:** Whitenoise, Debug Toolbar, Django Extensions, Corsheaders

---

## **Configuração do Ambiente**
1. Clonar o repositório:
   ```bash
   git clone <seu-repo-url>
   cd twitter-clone

2. Criar e ativar o ambiente virtual:

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


3. Instalar dependências:

pip install -r requirements.txt


4. Configurar variáveis de ambiente em .env.dev:

SECRET_KEY=your_secret_key
DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=twitter_clone
SQL_USER=carlos09
SQL_PASSWORD=admin09
SQL_HOST=127.0.0.1
SQL_PORT=5432


5. Criar e aplicar migrações:

python manage.py makemigrations
python manage.py migrate


6. Criar superusuário:

python manage.py createsuperuser


7. Rodar o servidor local:

python manage.py runserver