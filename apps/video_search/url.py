from django.urls import path
from apps.video_search.views import VideoProjectApi, SearchVideoApi, SearchVideoResultsApi

urlpatterns = [
    path('video-project/', VideoProjectApi.as_view()),
    path('video-project/<int:id>/', VideoProjectApi.as_view()),
    path('video-project/<int:project_id>/search/', SearchVideoApi.as_view()),
    path('video-project/<int:project_id>/search/results/', SearchVideoResultsApi.as_view()),
]