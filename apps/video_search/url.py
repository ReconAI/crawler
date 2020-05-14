from django.urls import path
from apps.video_search.views import VideoProjectApi, SearchVideoApi

urlpatterns = [
    path('video-project/', VideoProjectApi.as_view()),
    path('video-project/<int:id>/', VideoProjectApi.as_view()),
    path('video-project/<int:id>/search/', SearchVideoApi.as_view()),
]