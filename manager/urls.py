from django.urls import path
from .views import GetPlaylistView

urlpatterns = [
    path('get_playlist/', GetPlaylistView.as_view(), name='get_playlist'),
]