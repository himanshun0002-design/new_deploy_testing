"""
WSGI config for socity_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socity_project.settings_prod')

application = get_wsgi_application()

# For debugging purposes
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000...')
    httpd.serve_forever()
