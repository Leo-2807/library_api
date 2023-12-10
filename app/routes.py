from flask import Flask, request, jsonify
from app.models import db, Book
from sqlalchemy.exc import IntegrityError

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.route('/api/books', methods=['GET'])
    def get_all_books():
        try:
            books = Book.query.all()
            return jsonify([book.as_dict() for book in books])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/books', methods=['POST'])
    def add_new_book():
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])

        try:
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': 'Book added successfully!'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Duplicate book entry'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/api/books/<int:id>', methods=['PUT'])
    def update_book(id):
        data = request.get_json()
        try:
            book = Book.query.get(id)
            if book:
                book.title = data['title']
                book.author = data['author']
                db.session.commit()
                return jsonify({'message': 'Book updated successfully!'})
            else:
                return jsonify({'error': 'Book not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    @app.route('/api/books/<int:id>', methods=['DELETE'])
    def delete_book(id):
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'deleted'})

    return app
