import factory

from apps.video_search.models import VideoProject


class VideoProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VideoProject
