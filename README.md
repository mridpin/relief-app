# Relief APP
This app is the server side of the Video Viewer web application.

## Requirements
- Python 3.9
- Pip
- Pipenv
- Storage: default sqlite packaged with Django

## How to run
1. Clone the repo
2. Run the python virtual environment with
`python3 -m pipenv shell`
3. Download dependencies with `pip3 install -r requirements.txt`
4. Run with `python3 manage.py runserver`, server will listen on `localhost:8000`

## API endpoints
1. GET /bookmark/: returns list of bookmarks
2. GET /history/: returns list of history
3. POST /bookmark/: creates a bookmark and adds it to the database
4. POST /history/: creates a history item and adds it to the database
5. DELETE /bookmark/: deletes a bookmark item from the database



## Extra features
1. Bookmark delete endpoint
