import unittest
from flask import json
from run import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_all_books(self):
        response = self.app.get('/api/books')
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_add_new_book(self):
        book_data = {'title': 'Percy Jackson', 'author': 'Rick Riordan'}
        response = self.app.post('/api/books', json=book_data)
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Book added successfully!')
    
    def test_update_book(self):
        book_data = {'title': 'Jujutsu Kaisen', 'author': 'Gege Akutami'}
        response = self.app.put('/api/books/1', json=book_data)
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Book updated successfully!')
    
    #def test_delete_book(self):
    #   self.app.delete('api/books/4')


if __name__ == '__main__':
    unittest.main()
