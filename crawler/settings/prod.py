from crawler.settings.common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_crawler_prod',
        'USER': 'postgres',
        'PASSWORD': 'pVWYDdQuLnuVAkG8RpWb',
        'HOST': 'crawler-database.ccpn7fr8v2y9.us-east-2.rds.amazonaws.com',
        'PORT': 5432,
    }
}