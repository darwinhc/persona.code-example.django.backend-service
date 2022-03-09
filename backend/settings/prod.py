import os
# Local
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# PNLMw4a2DFrspJzb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'persona',
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '3306',
    }
}


STATIC_URL = 'static/'


django_heroku.settings(locals())