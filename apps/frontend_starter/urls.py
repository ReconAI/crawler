from django.urls import path

from apps.frontend_starter import views

urlpatterns = [
    path('results', views.search_results, name='results'),
    path('', views.index, name='index'),
]
