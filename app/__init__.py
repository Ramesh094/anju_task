from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_restful import Api
from config.config import Config, Config2
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.config.from_object(Config2)
mongo = PyMongo(app)
api = Api(app)
auth = HTTPBasicAuth()

from app.views.resource import RegisterResource, ProductList, Product

api.add_resource(RegisterResource, '/register')
api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<int:product_id>')
