from app.models.model import User
from app import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash


class Controller:
    @staticmethod
    def user_exists(username):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return None
        return user


    @staticmethod
    def create_user(username, password):
        try:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except IntegrityError as e:
            db.session.rollback()
            return {'msg': f'User with {username} already exists'}

