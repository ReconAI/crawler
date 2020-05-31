from django.db import models

from common.enum import ChoiceEnum


class VideoStatusEnum(ChoiceEnum):
    CONFIRMED = 'CONFIRMED'
    DISCARDED = 'DISCARDED'

class VideoProject(models.Model):
    name = models.CharField(max_length=255, help_text='name of project')

class VideoSearchResult(models.Model):
    project = models.ForeignKey(VideoProject, on_delete=models.CASCADE)
    source_link = models.URLField(help_text='Source vimeo/youtube link')
    link = models.FileField(upload_to='', null=True, help_text='saved link to our storage')
    preview_link = models.FileField(upload_to='', null=True, help_text='saved link for preveiw to our storage')
    status = models.CharField(choices=VideoStatusEnum.for_choice(), null=True, max_length=100)
