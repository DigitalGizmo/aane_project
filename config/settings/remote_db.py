"""
Local Django settings for aane project.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aanedata',
        'USER': 'aanedata_user',
        'PASSWORD': get_secret("DB_PASS"),
        'HOST': '68.169.61.104', # eApps remote
        'PORT': '5432',
    }
}

# Application definition
# only adds mod_wsgi.server
# may not use wsgi express -- don't know how to use it with multiple settings files
#INSTALLED_APPS += ('mod_wsgi.server', )

