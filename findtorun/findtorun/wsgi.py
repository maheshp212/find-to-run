"""
WSGI config for findtorun project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

try:
    site.addsitedir('/home/ubuntu/envfind/lib/python3.5/site-packages')
    sys.path.append('/home/ubuntu/find-to-run/findtorun')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "findtorun.settings")
    activate_env = os.path.expanduser('/home/ubuntu/envfind/bin/activate_this.py')
    exec(compile(open(activate_env).read(),activate_env,'exec'), dict(__file__=activate_env))
except Exception as e:
    print('Exception occured')
    print(e)
    sys.exit(-1)


application = get_wsgi_application()
