from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def as_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author}
