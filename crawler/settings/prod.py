from crawler.settings.common import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://2f7043e70e054555b2380583a7909a86@o60297.ingest.sentry.io/5258876",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


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

SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME = 'prod-crawler-download-video-file-queue'
CELERY_TASK_DEFAULT_QUEUE = 'prod-celery-default'
CELERY_TASK_ROUTES = {
    'apps.video_search.tasks.*': {'queue': SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME}
}

PROXIES = [
    'http://LF25xM2mle:vpdnAAoiIs@45.156.150.26:57969'
    'http://LF25xM2mle:vpdnAAoiIs@45.156.150.22:57969',
    'http://LF25xM2mle:vpdnAAoiIs@45.156.150.11:57969',
    'http://LF25xM2mle:vpdnAAoiIs@45.156.150.25:57969',
    'http://LF25xM2mle:vpdnAAoiIs@45.156.150.24:57969',
]