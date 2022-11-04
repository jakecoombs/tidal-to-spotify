import os

from dotenv import load_dotenv

from Spotify import Spotify
from TidalMigration import TidalMigration

load_dotenv()

# Log in to Tidal - done
# Log in to Spotify - done

# 1. Transfer favourite songs
# Get tracks from Tidal - done
# Map by Artist -> Album -> Song
# Get liked songs from spotify - done
# Map by Artist -> Album -> Song
# Filter out any duplicates
# Add remaining songs to liked songs in Spotify

# 2. Transfer playlists
# Get playlists from Tidal
# For each playlist in Tidal
# Create empty playlist in Spotify with same name
# Search for song in spotify
# Add song to playlist


def main():
    print("Starting transfer from Tidal to Spotify...")
    migration = TidalMigration()
    print("Transfer complete.")


if __name__ == "__main__":
    main()
