import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from utils import stripTrackName

load_dotenv()


class Spotify:
    def __init__(self, scope="user-library-read"):
        print("Logging into Spotify...")
        self.session = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        print("Spotify login successful.")

    def getSavedTracks(self):
        # There is a max limit of 50 songs per request
        savedTracks: list[any] = []
        complete = False
        offset = 0
        while not complete:
            savedTracksObject = self.session.current_user_saved_tracks(50, offset)
            items = savedTracksObject["items"]
            savedTracks.extend(items)

            if len(items) < 50:
                complete = True
            offset += 50

        return savedTracks

    def mapSavedTracksByArtist(self, tracks):
        artistMap = {}

        for track in tracks:
            artist = track["track"]["artists"][0]["name"].lower()
            strippedTrackName = stripTrackName(track["track"]["name"])
            if artist in artistMap:
                artistMap[artist].append(strippedTrackName)
            else:
                artistMap[artist] = [strippedTrackName]

        return artistMap
