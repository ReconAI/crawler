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

SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME = 'prod-crawler-download-video-file-queue'
CELERY_TASK_DEFAULT_QUEUE = 'prod-celery-default'
CELERY_TASK_ROUTES = {
    'apps.video_search.tasks.*': {'queue': SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME}
}