from Spotify import Spotify
from Tidal import Tidal


class TidalMigration:
    def __init__(self):
        self.tidalAccount = Tidal()
        self.spotifyAccount = Spotify()

    def migrateFavouriteTracks(self):
        # Get Tidal tracks
        print("Getting favourite tracks from Tidal...")
        tidalTracks = self.tidalAccount.getFavouriteTracks()

        # Map Tidal tracks to artist -> song
        print(f"Mapping {len(tidalTracks)} Tidal tracks...")
        mappedTidalTracks = self.tidalAccount.mapFavouriteTracksByArtist(tidalTracks)

        # Get Spotify tracks
        print("Getting favourite tracks from Spotify...")
        spotifyTracks = self.spotifyAccount.getSavedTracks()

        # Map Spotify tracks to artist -> song
        print(f"Mapping {len(spotifyTracks)} Spotify tracks...")
        mappedSpotifyTracks = self.spotifyAccount.mapSavedTracksByArtist(spotifyTracks)

        # Filter for duplicate tracks
        print("Filtering duplicate tracks...")

        # Add remaining songs to liked songs in Spotify
        print("Liking missing songs in Spotify...")
