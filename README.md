# LIBRARY API

## Running the Application:

1. Clone the Repository:
```bash
git clone https://github.com/Leo-2807/library_api
cd library_api
```
2. Install dependencies:
```bash
pip3 install -r requirements.txt
```
3. Initialize the database:
```bash
python3
from app.routes import create_app
from app.db import db
app = create_app()
app.app_context().push()
db.create_all()
exit()
```
4. Run the application
```bash
python3 run.py
```
The command will start the application which can be viewed on `localhost:5000/api/books`.
![pic](https://github.com/Leo-2807/library_api/blob/main/pics/WhatsApp%20Image%202023-12-10%20at%2018.54.27_79a8449e.jpg)

Note:
I used virtual enviourment while making this api and so if you want to do the same then run the following command before installing the dependencies, in the project directory.
```bash
python3 -m venv .venv
.venv/lib/activate
```

## API Documentation

1. Retrieve All Books:
  * Endpoint: `GET /api/books`
⋅⋅* Response:
```json
[{'author': 'J.K.Rolling', 'id': 1, 'title': 'Harry Potter'}, {'author': 'Rick Riordan', 'id': 2, 'title': 'Percy Jackson'}, {'author': 'Ruskin Bond', 'id': 3, 'title': 'Blue Umbrella'}]
```

2. Add a New Book:
* Endpoint: `POST /api/books`
* Request Body:
```json
{'title': 'Percy Jackson', 'author': 'Rick Riordan'}
```
* Response:
```json
{'message': 'Book added successfully!'}
```

3. Update Book Details:
* Endpoint: `PUT /api/books/{id}`
* Request Body:
```json
{'title': 'Jujutsu Kaisen', 'author': 'Gege Akutami'}
```
* Response:
```json
{'message': 'Book updated successfully!'}
```

## Testing

The application creates an SQLite database file (`library.db`).
The file `tests/test_routes.py` can be used to test all the end points. To test one specific endpoint the other parts can be commented out.
```bash
python -m unittest tests/test_routes.py
```

## Additional

I created a fourth end point to delete books with their specific id. This endpoint does not have any error handling as it was used for testing only.

Endpoint: `DELETE /api/books/{id}`
