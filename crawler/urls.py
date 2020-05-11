from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.video_search.url')),
    path('', include('apps.frontend_starter.urls'))

]
