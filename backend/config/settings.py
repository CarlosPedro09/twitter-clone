import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Carregar variáveis do .env (local ou Vercel)
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env.dev")

BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default")
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Permitir o domínio da Vercel, Render e localhost
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,seu-backend.onrender.com"
).split(",")

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceiros
    "rest_framework",
    "rest_framework.authtoken",
    "django_extensions",
    "debug_toolbar",
    "whitenoise.runserver_nostatic",
    "corsheaders",

    # Apps do projeto
    "users",
    "tweets",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "backend.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.config.wsgi.application"

# Banco de dados (Postgres online via URL)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

# Auth customizado
AUTH_USER_MODEL = "users.CustomUser"

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Arquivos estáticos e mídia
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Whitenoise para servir arquivos estáticos no deploy
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}

# Debug toolbar
INTERNAL_IPS = ["127.0.0.1"]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React local
    "https://seu-frontend.vercel.app",  # Frontend na Vercel
]
# CORS_ALLOW_ALL_ORIGINS = True  # opcional, só se necessário

