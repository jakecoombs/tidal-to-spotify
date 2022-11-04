from Spotify import Spotify
from Tidal import Tidal


class TidalMigration:
    def __init__(self):
        self.tidalAccount = Tidal()
        self.spotifyAccount = Spotify()

    def migrateFavouriteTracks(self):
        # Get Tidal tracks
        tidalTracks = self.tidalAccount.getFavouriteTracks()

        # Map Tidal tracks to something useful

        # Get Spotify tracks
        spotifyTracks = self.spotifyAccount.getSavedTracks()

        # Map Spotify tracks to same object strucure as mapped Tidal tracks

        # Filter for duplicate tracks
