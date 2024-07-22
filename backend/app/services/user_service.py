from app.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(data):
    name = data.get("name")
    email = data.get("email")
    password = generate_password_hash(data.get("password"))
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def login_user(data):
    email = data.get("email")
    password = generate_password_hash(data.get("email"))
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
