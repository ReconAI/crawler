from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/', include('apps.video_search.url')),
    path('', include('apps.frontend_starter.urls'))

]

# static. Temporary for gunicorn
urlpatterns += staticfiles_urlpatterns()
