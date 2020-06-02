from crawler.settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_crawler_dev',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': '192.168.88.245',
        'PORT': 5436,
    }
}

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
CELERY_BROKER_URL=''

SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME = 'example-crawler-download-video-file-queue'
CELERY_TASK_DEFAULT_QUEUE = 'example-celery-default'
CELERY_TASK_ROUTES = {
    'apps.video_search.tasks.*': {'queue': SQS_CRAWLER_DOWNLOAD_VIDEO_FILE_QUEUE_NAME}
}