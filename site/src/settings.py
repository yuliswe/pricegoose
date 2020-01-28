"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=)j#hxj%&js=qd4xc_sxl1!g--@fn1n0d8ptm^c40l#!@y-h7h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# Application definition
SITE_APPS = [
    'src.common',
]

AUTH_USER_MODEL = 'common.User'

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',  # 提供authentication
    # https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes
    'django.contrib.contenttypes',  # 提供authentication
    'django.contrib.sessions',  # 提供request.user
    # https://docs.djangoproject.com/en/2.2/topics/http/sessions/
    'django.contrib.messages',  # 在网站显示消息
    # https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
    'django.contrib.staticfiles',  # 提供网站css, js
    'django_extensions',  # 提供manage.py runscript
    # https://django-extensions.readthedocs.io/en/latest/index.html
    'rest_framework',
    # https://www.django-rest-framework.org/
] + SITE_APPS

MIGRATION_MODULES_ROOT = Path(os.environ['MIGRATION_MODULE_DIR']) / 'migrations'
MIGRATION_MODULES = {
    'common': 'migrations.common'
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

STATIC_URL = '/static/'
STATIC_ROOT = Path(os.environ['VAR_DIR']) / 'collectstatic'
STATICFILES_DIRS = [
    BASE_DIR / 'web' / 'static',
    os.environ['WEBPACK_OUTPUT_DIR'],
]

TEMPLATE_LIBS = {}
for path in BASE_DIR.glob('web/**/tags/*.py'):
    if path.stem != '__init__':
        TEMPLATE_LIBS[path.stem] = str(path.relative_to(
            BASE_DIR.parent).with_suffix('')).replace('/', '.')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'web',
            BASE_DIR / 'api/notifications'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': TEMPLATE_LIBS,
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'site',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = 'pricedropca@gmail.com'

EMAIL_HOST_PASSWORD = 'Droppie123'
