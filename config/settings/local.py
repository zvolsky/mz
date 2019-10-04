from .base import INSTALLED_APPS, DATABASES


DEBUG = True
POSTGRES = True  # mz setting

INSTALLED_APPS += (
    'django_extensions',
)

if POSTGRES:
    DATABASES['default'].update({
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 1800,
        'HOST': '',
        'PORT': 5432,
        'NAME': 'mz',
        'USER': 'mz',
    })
