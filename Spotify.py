import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


class Spotify:
    def __init__(self, scope="user-library-read"):
        print("Logging into Spotify...")
        self.session = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        print("Spotify login successful.")

    def getSavedTracks(self):
        savedTracksObject = self.session.current_user_saved_tracks()
        return savedTracksObject["items"]
