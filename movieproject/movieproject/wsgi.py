"""
WSGI config for movieproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

import django
from django.core.wsgi import get_wsgi_application

from django.core.management import call_command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproject.settings')

django.setup()
call_command("migrate", interactive=False)
application = get_wsgi_application()
