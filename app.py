import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return "You need to submit data.", 400
    else:
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        album = Album(
            None,
            request.form['title'],
            request.form['release_year'],
            request.form['artist_id'])
        repository.create(album)
        return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join(f"{album}" for album in albums)
















# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

