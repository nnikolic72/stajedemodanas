"""
WSGI config for stajedemodanas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

from configurations.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stajedemodanas.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')
application = get_wsgi_application()
