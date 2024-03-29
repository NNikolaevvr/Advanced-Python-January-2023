from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        album = [alb for alb in self.albums if alb.name == album_name]

        if album:
            if album[0].published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album[0])
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        album_details = '\n'.join([album.details() for album in self.albums])
        return f"Band {self.name}\n{album_details}"
