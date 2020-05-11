from django.db import models


class VideoProject(models.Model):
    name = models.CharField(max_length=255, help_text='name of project')
