import os
from typing import Any

import tidalapi
from dotenv import load_dotenv
from tidalapi.artist import Artist
from tidalapi.media import Track

load_dotenv()


class Tidal:
    def __init__(self):
        print("Logging into Tidal...")
        self.session = tidalapi.Session()
        try:
            self.session.load_oauth_session(
                os.environ["TOKEN_TYPE"],
                os.environ["ACCESS_TOKEN"],
                os.environ["REFRESH_TOKEN"],
                os.environ["EXPIRY_TIME"],
            )
        except Exception:
            # Could not login using stored credentials
            self.session.login_oauth_simple()
            self.listCredentials()

        print("Tidal login successful.")

        self.user = tidalapi.user.User(self.session, self.session.user.id)
        self.favourites = tidalapi.user.Favorites(self.session, self.user.id)
        self.playlists: list(tidalapi.Playlist) = tidalapi.user.LoggedInUser(
            self.session, self.user.id
        ).playlists()

    def listCredentials(self):
        print(
            "It is recommended to store the following credentials in a .env file, this removes the need to login through the browser."
        )
        print("Tidal Login Credentials:\n")
        print(f"TOKEN_TYPE={self.session.token_type}")
        print(f"ACCESS_TOKEN={self.session.access_token}")
        print(f"REFRESH_TOKEN={self.session.refresh_token}")
        print(f"EXPIRY_TIME={self.session.expiry_time}")

    def getFavouriteTracks(self):
        # Returns list of tracks of type tidalapi.media.Track
        return self.favourites.tracks()

    def mapFavouriteTracksByArtist(self, tracks: list[Track]):
        artistMap: dict[str, list[str]] = {}

        for track in tracks:
            trackArtist: Artist = track.artist
            if trackArtist.name in artistMap:
                artistMap[trackArtist.name].append(track.name)
            else:
                artistMap[trackArtist.name] = [track.name]

        return artistMap
