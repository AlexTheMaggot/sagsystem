# ExternalImports
import os
from pathlib import Path
# End ExternalImports

# BaseDir
BASE_DIR = Path(__file__).resolve().parent.parent
# End BaseDir

# SecretKey
SECRET_KEY = '96yol=1zc0fq04-n^1v_dgocl17a9b5%umpt-8u)_&ptcycxc7'
# End SecretKey

# Debug
DEBUG = True
# End Debug

# AllowedHosts
ALLOWED_HOSTS = ['*', ]
# End AllowedHosts

# InstalledApps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp.apps.MainappConfig',
    'incidents.apps.IncidentsConfig',
    'tender.apps.TenderConfig',
    'customers.apps.CustomersConfig',
]
# End InstalledApps

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# End Middleware

# RootUrlConf
ROOT_URLCONF = 'sagsystem.urls'
# End RootUrlConf

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# End Templates

# WSGIApplication
WSGI_APPLICATION = 'sagsystem.wsgi.application'
# End WSGIApplication

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# End Databases

# AuthPasswordValidators
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
# End AuthPasswordValidators

# Language
LANGUAGE_CODE = 'ru'
# End Language

# TimeZone
TIME_ZONE = 'Asia/Samarkand'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# End TimeZone

# StaticAndMedia
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainapp/static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mainapp/media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
# End StaticAndMedia
