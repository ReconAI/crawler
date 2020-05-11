from django.urls import path
from apps.video_search.views import VideoProjectApi

urlpatterns = [
    path('video-project/', VideoProjectApi.as_view()),
]