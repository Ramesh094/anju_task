class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Learn9998@localhost/task'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config2:
    MONGO_URI = 'mongodb://localhost:27017/product_db'
