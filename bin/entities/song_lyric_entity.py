class Song:
    def __init__(self, song, song_link, artist, artist_link, album, album_link):
        self.song = song
        self.song_link = song_link
        self.artist = artist
        self.artist_link = artist_link
        self.album = album
        self.album_link = album_link

    @classmethod
    def from_json(cls, json_data):
        """
        Factory method to create a Song object from JSON data.
        """
        try:
            result = json_data["results"]["result"]
            return cls(
                song=result.get("song", "N/A"),
                song_link=result.get("song-link", "N/A"),
                artist=result.get("artist", "N/A"),
                artist_link=result.get("artist-link", "N/A"),
                album=result.get("album", "N/A"),
                album_link=result.get("album-link", "N/A"),
            )
        except (KeyError, TypeError) as e:
            print(f"Error parsing JSON: {e}")
            return None

    def __repr__(self):
        """
        Returns a string representation of the Song object.
        """
        return (
            f"Song(song='{self.song}', "
            f"song_link='{self.song_link}', "
            f"artist='{self.artist}', "
            f"artist_link='{self.artist_link}', "
            f"album='{self.album}', "
            f"album_link='{self.album_link}')"
        )

    def to_dict(self):
        """
        Converts the Song object back to a dictionary.
        """
        return {
            "song": self.song,
            "song-link": self.song_link,
            "artist": self.artist,
            "artist-link": self.artist_link,
            "album": self.album,
            "album-link": self.album_link,
        }
