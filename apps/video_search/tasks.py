"""
Celery tasks
"""
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

from apps.video_search.models import VideoSearchResult
from common.utils import PreviewDispatcher, VideoDownloader
from django.core.files import File

logger = get_task_logger(__name__)


@shared_task
def task_save_source_video_and_create_preview(project_id, link):
    logger.info('Url=%s' % link)
    out_filepath, out_filename = VideoDownloader().download(link)
    preview_link, preview_filename = PreviewDispatcher().make_video(out_filepath)

    # save to S3
    f = open(out_filepath, 'rb')
    myfile = File(f, name=out_filename)
    preview_file = File(open(preview_link, 'rb'), name=preview_filename)
    VideoSearchResult.objects.create(
        project_id=project_id,
        source_link=link,
        link=myfile,
        preview_link=preview_file,
    )
