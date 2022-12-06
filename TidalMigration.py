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
        filteredTracks = self.filterDuplicateTracks(
            mappedTidalTracks, mappedSpotifyTracks
        )

        # Add remaining songs to liked songs in Spotify
        print(
            f"Saving missing songs of {len(filteredTracks.keys())} artists in Spotify...\n"
        )
        self.spotifyAccount.saveTracksWithMap(filteredTracks)

    def filterDuplicateTracks(
        self, tidalTracks: dict[str, list[str]], spotifyTracks: dict[str, list[str]]
    ) -> dict[str, list[str]]:
        missingTracks = {}

        # If a song is present in both Spotify and Tidal, remove it from the list
        for artist in tidalTracks:
            if artist not in spotifyTracks:
                missingTracks[artist] = tidalTracks[artist]
                continue

            missingSongs = list(
                set(tidalTracks[artist]).symmetric_difference(
                    set(spotifyTracks[artist])
                )
            )

            if len(missingSongs) > 1:
                missingTracks[artist] = missingSongs

        return missingTracks
