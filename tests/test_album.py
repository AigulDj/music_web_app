from lib.album import Album

"""
Constructs with id, release date and artist id
"""
def test_constracts():
    album = Album(1, "Test Title", 2000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 2