import sys
from pathlib import Path

# from unipath import Path

import json
from django.core.exceptions import ImproperlyConfigured

# BASE_DIR = Path(__file__).ancestor(3)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Add apps directory to Python path
sys.path.insert(0, str(BASE_DIR / 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
# JSON-based secrets module
with open(BASE_DIR / 'config' / 'settings' / 'secrets.json') as f:
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
DEBUG = False

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['aane.deerfield-ma.org', 'aane-temp.deerfield-ma.org', '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition
INSTALLED_APPS = (
    'people.apps.PeopleConfig',
    'sources.apps.SourcesConfig',
    'sitewide.apps.SitewideConfig',
    'locations.apps.LocationsConfig',
    'about.apps.AboutConfig',
    # 'django_quill',
    'django_htmx',
    'tinymce',
    # 'graphene_django',
    'rest_framework',
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


ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

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
STATIC_ROOT = BASE_DIR.parent / "aane_static"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / "local_static",
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

TINYMCE_DEFAULT_CONFIG = {
    "height": "350px",
    "width": "960px",
    "menubar": "false",
    "plugins": "lists link visualblocks code code help wordcount charmap", 
    # These require paid plugins:  paste spellchecker
    "toolbar": "undo redo | bold italic superscript |  fontsizeselect | outdent indent |  numlist bullist | pagebreak | charmap emoticons | "
    "save |   codesample | code",
    # underline strikethrough link anchor
    "custom_undo_redo_levels": 10,
    # "language": "es_ES",  # To force a specific language instead of the Django current language.
    "charmap": [
        [163, 'pound sign'],
        [8364, 'euro sign'],
        [36, 'dollar sign'],
        [162, 'cent sign'],
        # [165, 'yen sign'],
        [8211, 'en dash'],
        [8212, 'em dash'],
        # [8216, 'left single quotation mark'],
        # [8217, 'right single quotation mark'],
        # [8220, 'left double quotation mark'],
        # [8221, 'right double quotation mark'],
    ],
}