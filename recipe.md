# Single Table Design Recipe Template

Test-drive a route GET /artists, which returns the list of artists:
Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


Test-drive a route POST /artists, which creates a new artist in the database. Your test should verify the new artist is returned in the response of GET /artists.
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| album                 | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `artist_id`, `id`

## 3. Decide the column types

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```


# Plain Route Route Design Recipe


## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
  title: string
  release_year: number (str)
  artist_id: number (str)

  GET /albums
```

## 2. Create Examples as Tests

```python
# Scenario 1

    # POST /albums
    # title: 'Rock Album 2020'
    # release_year: 2020
    # artist_id: 1
    # Expected Response (200 OK)
    """(No content)"""

    # GET /albums
    # Expected Response (200 OK)
    """
    Album(1, 'Rock Album 2020', 2020, 1);
    Album(2, 'Pop Album 2019', 2019, 2);
    Album(3, 'Hip-Hop Album 2021', 2021, 3);
    Album(4, 'Jazz Album 2018', 2018, 4);
    Album(5, 'Classical Album 2017', 2017, 1);
    """

# Scenario 2

    # POST /albums
    
    # Expected Response (404 Bad Request)
    """
    You need to submit data.
    """

    # GET /albums
    # Expected Response (200 OK)
    """
    Album(1, 'Rock Album 2020', 2020, 1);
    Album(2, 'Pop Album 2019', 2019, 2);
    Album(3, 'Hip-Hop Album 2021', 2021, 3);
    Album(4, 'Jazz Album 2018', 2018, 4);
    Album(5, 'Classical Album 2017', 2017, 1);
    """

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```
