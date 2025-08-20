"""
WSGI config for aane project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/

Deployed instances (dev and prod on eApps) will have mod_wsgi active, as configured in 
httpd.conf, to have the appropriate process_group name.

Otherwise this will use the local settings.
Some devel envs won't need or have mod_wsgi
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")
application = get_wsgi_application()
