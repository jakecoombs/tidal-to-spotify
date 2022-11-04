# Transfer Tidal Data to Spotify

**⚠️⚠️WORK IN PROGRESS ⚠️⚠️**

Transfer your Tidal Data to Spotify using Python.

This Python script will transfer all of your favourite tracks and playlists from Tidal and transfer them over to Spotify (hopefully without duplicates).

## Prequisites

1. Must have Python installed.
2. Must have an app set up through [Spotify Developers](https://developer.spotify.com/dashboard/applications).

## Setup

1. Create a new .env file at the root of the directory.
2. Add new environment variables `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` with the Client ID and Client Secret values for your Spotify Application.
3. Add a new redirect URI to your Spotify Application in its settings.
4. Add the same redirect URI value to the .env file using the key `SPOTIPY_REDIRECT_URI`.
5. Install required packages.

```

pip install -r requirements.txt

```

## Start the transfer

```
python main.py
```
