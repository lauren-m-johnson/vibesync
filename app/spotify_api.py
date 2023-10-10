from dotenv import load_dotenv
import os
import base64
import json
import requests
from requests import post, get

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def search_for_playlist(token, playlist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + token}
    params = {'q': playlist_name, 'type': 'playlist', 'limit': 1}

    response = requests.get(url, headers=headers, params=params)
    json_result = response.json()
    playlists = json_result['playlists']['items'] if 'playlists' in json_result else []
    return playlists

def get_playlist_details(token, playlist_id):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    headers = {'Authorization': 'Bearer ' + token}

    response = requests.get(url, headers=headers)
    json_result = response.json()
    return json_result

token = get_token()
playlists = search_for_playlist(token, 'Happy Folk')

# Check if there are any playlists returned
if playlists:
    # Extract the id of the first playlist
    playlist_id = playlists[0]['id']
    playlist_details = get_playlist_details(token, playlist_id)
    print(playlist_details)
else:
    print("No playlists found.")