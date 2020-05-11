from django.urls import path

from apps.frontend_starter import views

urlpatterns = [
    path('', views.index, name='index'),
]
