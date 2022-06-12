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
username = 'rqfju899d4ie81memjx0fgy70'

client_auth_response = requests.post(
    url=f'https://accounts.spotify.com/api/token', 
    auth=HTTPBasicAuth(client_id, client_secret), 
    data={'grant_type': 'client_credentials'})

if not client_auth_response.ok:
    raise RuntimeError(f'There was a problem retrieving application credentials from spotify: \n\t{client_auth_response.content}')

access_token = client_auth_response.json()['access_token']
user_response = requests.get(f'https://api.spotify.com/v1/users/{username}', auth=BearerAuth(access_token))

user_data = user_response.json()
print(user_data)