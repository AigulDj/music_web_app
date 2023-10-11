from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all the albums in the albums table
"""
def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Pop Album 2019', 2019, 2),
        Album(2, 'Hip-Hop Album 2021', 2021, 3),
        Album(3, 'Jazz Album 2018', 2018, 4)
    ]

"""
When I call #create
I create an album in the database
And I can see it back in #all
"""
def test_create(db_connection):
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 2000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Pop Album 2019', 2019, 2),
        Album(2, 'Hip-Hop Album 2021', 2021, 3),
        Album(3, 'Jazz Album 2018', 2018, 4),
        Album(4, "Test Title", 2000, 2)
    ]
