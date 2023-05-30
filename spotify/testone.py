#!/usr/bin/env python3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

clientID = config['SPOTIPY_CLIENT_ID']
clientSecret = config['SPOTIPY_CLIENT_SECRET']
redirect_uri = 'http://localhost:8888/callback'
scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id=clientID,
          client_secret=clientSecret,
          redirect_uri=redirect_uri,    
          scope=scope, open_browser=False))

# Shows playing devices
res = sp.devices()
pprint(res)

def set_default_device():
    devices = sp.devices()

    if devices['devices']:
        default_device_id = devices['devices'][1]['id']
        sp.transfer_playback(device_id=default_device_id, force_play=True)
        print(f"Default device set to {default_device_id}")
    else:
        print("No devices found.")

set_default_device()

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=,
#                                                client_secret=config['SPOTIPY_CLIENT_SECRET'],
#                                                redirect_uri='http://localhost:8888/callback',
#                                                scope='user-read-playback-state,user-modify-playback-state'))

results = sp.search(q='Untouchable Face Ani Defranco', type='track', limit=1)
if results['tracks']['items']:
  track_uri = results['tracks']['items'][0]['uri']
  sp.start_playback(uris=[track_uri])
  print(f"Playing {results['tracks']['items'][0]['name']}")
else:
  print('No results found')