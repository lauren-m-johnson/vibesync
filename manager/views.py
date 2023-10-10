from django.shortcuts import render
from django.http import JsonResponse

def get_playlist(request):
    mood = request.GET.get('mood')
    # Use the mood to search for the playlist using your existing Spotify API functions
    # Return the playlist data as a JSON response
    playlist_data = get_playlist(mood) 
    return JsonResponse(playlist_data)

