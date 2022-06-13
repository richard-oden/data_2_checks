from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import os
import requests

#For use with bearer token authentication:
#https://stackoverflow.com/a/58055668/12326207
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

load_dotenv('.env')

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Authenticate application and get access token:
client_auth_response = requests.post(
    url=f'https://accounts.spotify.com/api/token', 
    auth=HTTPBasicAuth(client_id, client_secret), 
    data={'grant_type': 'client_credentials'})

if not client_auth_response.ok:
    raise RuntimeError(f'There was a problem retrieving application credentials from Spotify: \n\t{client_auth_response.content}')

access_token = client_auth_response.json()['access_token']

# Get albums by the band Knower:
artist_albums_info = requests.get(
    url='https://api.spotify.com/v1/artists/7fVp0A6oCMfiQJihMnY0SZ/albums', 
    auth=BearerAuth(access_token)).json()

album_ids = [item['id'] for item in artist_albums_info['items']]

albums = requests.get(
    url=f'https://api.spotify.com/v1/albums?ids={",".join(album_ids)}', 
    auth=BearerAuth(access_token)).json()

print(albums)