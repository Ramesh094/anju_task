from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.controller.user_controller import Controller
from app import auth
from app import mongo
from pymongo.errors import DuplicateKeyError

from flask import request, abort


class RegisterResource(Resource):
    def post(self):
        parser = RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        is_user_exist = Controller.user_exists(username)
        if is_user_exist:
            return {'message': f'An user is already exists with {username}'}, 409
        new_user = Controller.create_user(username, password)
        return {'message': f'New user with {new_user.username} is created successfully'}, 201

@auth.verify_password
def validate(username, password):
    user = Controller.user_exists(username)
    if user is None:
        abort(401, {"message": "User doesn't exist"})
        return None
    if user.check_password(password):
        return user
    else:
        abort(401, {"message": "Incorrect password"})
        return None


class ProductList(Resource):
    @auth.login_required
    def get(self):
        products = list(mongo.db.products.find({}, {'_id': 0}))
        if products:
            return {'products': products}, 200


    @auth.login_required
    def post(self):
        new_product = request.json
        try:
            mongo.db.products.insert_one(new_product)
            return {'message': 'Product added successfully'}, 201
        except DuplicateKeyError:
            return {'message': 'Duplicate key error'}, 409
        except Exception:
            return {'message': 'Failed to create record '}, 500

class Product(Resource):
    @auth.login_required
    def get(self, product_id):
        product = mongo.db.products.find_one({'_id': product_id}, {'_id': 0})
        if product:
            return product, 200
        return {'message': 'Product not found'}, 404

    @auth.login_required
    def put(self, product_id):
        updated_data = request.json
        try:
            result = mongo.db.products.update_one({'_id': product_id}, {'$set': updated_data})
            if result.modified_count == 1:
                return {'message': 'Product updated successfully'}, 200
        except DuplicateKeyError:
            return {'message': 'Duplicate key error'}, 409
        except Exception as e:
            return {'message': 'Product not updated'}, 500
        return {'message': 'Product not found'}, 404

    @auth.login_required
    def delete(self, product_id):
        result = mongo.db.products.delete_one({'_id': product_id})
        if result.deleted_count == 1:
            return {'message': 'Product deleted successfully'}, 200
        return {'message': 'Product not found'}, 404

