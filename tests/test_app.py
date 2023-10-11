"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Rock Album 2020',
        'release_year': '2020',
        'artist_id': '1'
        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Pop Album 2019, 2019, 2)\n" \
        "Album(2, Hip-Hop Album 2021, 2021, 3)\n" \
        "Album(3, Jazz Album 2018, 2018, 4)\n" \
        "Album(4, Rock Album 2020, 2020, 1)"

"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Pop Album 2019, 2019, 2)\n" \
        "Album(2, Hip-Hop Album 2021, 2021, 3)\n" \
        "Album(3, Jazz Album 2018, 2018, 4)"


def test_post_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit data."

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Pop Album 2019, 2019, 2)\n" \
        "Album(2, Hip-Hop Album 2021, 2021, 3)\n" \
        "Album(3, Jazz Album 2018, 2018, 4)" 
