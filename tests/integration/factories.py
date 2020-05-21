import factory

from apps.video_search.models import VideoProject, VideoSearchResult


class VideoProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VideoProject

class VideoSearchResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VideoSearchResult
