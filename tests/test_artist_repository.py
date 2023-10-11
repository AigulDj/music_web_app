from lib.artist_repository import ArtistRepository
from lib.artist import Artist


def test_create(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository(db_connection)
    artist = Artist('Wild nothing', 'Indie')
    repository.create(artist)
    assert repository.all() == [
        Artist('Pixies', 'Rock'),
        Artist('ABBA', 'Pop'),
        Artist('Taylor Swift', 'Pop'),
        Artist('Nina Simone', 'Jazz'),
        Artist('Wild nothing', 'Indie')
    ]
