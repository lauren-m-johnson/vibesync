from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from spotify_api import get_token, search_for_playlist, get_playlist_details

@method_decorator(csrf_exempt, name='dispatch')  
class GetPlaylistView(View):
    def post(self, request):
        mood = request.POST.get('mood')
        token = get_token()
        playlists = search_for_playlist(token, mood)

        if playlists:
            playlist_id = playlists[0]['id']
            playlist_details = get_playlist_details(token, playlist_id)
            return JsonResponse(playlist_details, safe=False)
        else:
            return JsonResponse({'error': 'No playlists found'}, status=500)