from app import app, db, mongo
from pymongo import ASCENDING
from app.models.model import User

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        mongo.db.products.create_index([("name", ASCENDING)], unique=True)
    app.run(debug=True)