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

"""
import os
try:
	import mod_wsgi
	try:
		os.environ['DJANGO_SETTINGS_MODULE'] = 'aane.settings.%s' % mod_wsgi.process_group
	except AttributeError:
		# let the above setting stand
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aane.settings.local")
except ImportError:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aane.settings.local")
	
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""

import os

"""
# fix for populate() isn't reentrant - run this to kill, the put
# back to normal
def application(environ, start_response):
    if environ['mod_wsgi.process_group'] != '': 
        import signal
        os.kill(os.getpid(), signal.SIGINT)
    return ["killed"]
"""


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aane.settings.staging")

application = get_wsgi_application()

