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
try:
	import mod_wsgi
	try:
		os.environ['DJANGO_SETTINGS_MODULE'] = 'impressions.settings.%s' % mod_wsgi.process_group
	except AttributeError:
		# let the above setting stand
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "impressions.settings.local")
except ImportError:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "impressions.settings.local")
	
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
