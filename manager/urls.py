from django.urls import path
from . import views

urlpatterns = [
    path('get_playlist', views.get_playlist, name='get_playlist'),
]