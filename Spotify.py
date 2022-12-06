import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

from utils import stripTrackName

load_dotenv()


class Spotify:
    def __init__(self, scope="user-library-read,user-library-modify"):
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

    def getTrackId(self, artist: str, songTitle: str) -> str | None:
        response = self.session.search(
            q=f"artist:{artist} track:{songTitle}", limit=1, type="track"
        )
        if response["tracks"]["total"] == 0:
            return None

        return response["tracks"]["items"][0]["id"]

    def saveTracksWithMap(self, artistTracksMap: dict[str, dict[str, str]]):
        failed = []
        trackIds = []
        for artist in artistTracksMap:
            songs = artistTracksMap[artist]
            for song in songs:
                trackId = self.getTrackId(artist, song)
                if trackId is None:
                    failed.append(f"'{song}' by '{artist}'")
                else:
                    trackIds.append(trackId)

        for track in failed:
            print(f"Unable to find {track}.")

        if len(trackIds) > 0:
            print(f"\nSaving {len(trackIds)} songs.")
            self._saveTracks(trackIds)

    def _saveTracks(self, ids: list[str]):
        # A maximum of 50 ids can be parsed in a single request
        (div, mod) = divmod(len(ids), 50)

        if mod > 0:
            div += 1

        # Loop for number of requests
        for i in range(div):
            start = i * 50

            end = (i + 1) * 50
            if i > 0:
                end -= 1

            self.session.current_user_saved_tracks_add(ids[start:end])
