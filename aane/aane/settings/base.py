"""
Django settings for aane project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# this call is now (with 3-tier approach) one level deeper, so ..
# Using Unipath per Two Scoops
from unipath import Path
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).ancestor(3)

# SECURITY WARNING: keep the secret key used in production secret!
# JSON-based secrets module
with open(BASE_DIR.child('aane', 'settings', 'secrets.json')) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """ Get the secret variable or return explicit exception. """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['aane.deerfield-ma.org', '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition
INSTALLED_APPS = (
    'people.apps.PeopleConfig',
    'sources.apps.SourcesConfig',
    'locations.apps.LocationsConfig',
    'about.apps.AboutConfig',
    'django_quill',
    'django_htmx',
    # 'graphene_django',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'aane.urls'

WSGI_APPLICATION = 'aane.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# print("db_pass: ", get_secret("DB_PASS"))

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aanedata',
        'USER': 'aanedata_user',
        'PASSWORD': get_secret("DB_PASS"),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)    

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR.ancestor(2).child("aane_static")

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child("local_static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child("templates")],
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

# For Django 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# GRAPHENE = {
#     "SCHEMA": "aane.schema.schema"
# }
