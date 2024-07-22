from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tests = db.relationship('Test', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }


class Notebook(db.Model):
    __tablename__ = 'notebooks'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), nullable=False)
    tests = db.relationship('Test', backref='notebook', lazy=True)

    def __repr__(self):
        return f'<Notebook {self.model}>'

    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'solution': self.solution,
            'answer': self.answer
        }


class TestTag(db.Model):
    __tablename__ = 'testtags'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    tests = db.relationship('Test', backref='testtag', lazy=True)

    def __repr__(self):
        return f'<TestTag {self.description}>'

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description
        }


class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.id'), nullable=False)
    testtag_id = db.Column(db.Integer, db.ForeignKey('testtags.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    test_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Test {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'notebook_id': self.notebook_id,
            'testtag_id': self.testtag_id,
            'score': self.score,
            'test_date': self.test_date.isoformat()
        }
