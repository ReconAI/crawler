"""
Celery tasks
"""
from __future__ import absolute_import, unicode_literals

import os
from celery import shared_task
from celery.utils.log import get_task_logger

from apps.video_search.models import VideoSearchResult
from common.utils import PreviewDispatcher, VideoDownloader
from django.core.files import File

logger = get_task_logger(__name__)


@shared_task
def task_save_source_video_and_create_preview(video_search_result_id):
    logger.info('video_search_result_id=%s' % video_search_result_id)

    try:
        video_search_result = VideoSearchResult.objects.filter(id=video_search_result_id).get()
        out_filepath, out_filename = VideoDownloader().download(video_search_result.source_link)
        preview_filepath, preview_filename = PreviewDispatcher().make_video(out_filepath)

        # save to S3
        f = open(out_filepath, 'rb')
        dumped_file = File(f, name=out_filename)
        preview_file = File(open(preview_filepath, 'rb'), name=preview_filename)
        video_search_result.link = dumped_file
        video_search_result.preview_link = preview_file
        try:
            video_search_result.save()
        except Exception as e:
            logger.info("video_search_result_id=%s id deleted. Could not save video links" % video_search_result_id)

        # delete files from folder
        os.remove(out_filepath)
        os.remove(preview_filepath)
    except VideoSearchResult.DoesNotExist as e:
        logger.info("video_search_result_id=%s id deleted. Could not start video processing" % video_search_result_id)

