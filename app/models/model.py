from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     quantity = db.Column(db.Float, nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#     __table_args__ = (
#         db.CheckConstriant(quantity >= 0, name='quantity_min_value'),
#         db.CheckConstraint(rating >= 0, name='rating_min_value'),
#         db.CheckConstraint(rating <= 5, name='rating_max_value')
#     )

