import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def generateSpotify():
    cid = 'b774312c3dfb4b15a9dab8ef0f4a7f51'
    secret = '3bde03e4edec4d1abf81b059a9eabdbc'

    client_credentials_manager = SpotifyClientCredentials(cid,secret)

    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)