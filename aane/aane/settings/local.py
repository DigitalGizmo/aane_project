"""
Local Django settings for aane project.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition
# only adds mod_wsgi.server
# may not use wsgi express -- don't know how to use it with multiple settings files
#INSTALLED_APPS += ('mod_wsgi.server', )

