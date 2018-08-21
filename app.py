
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from application.resources.item import Item, ItemList
from application.resources.store import Store, StoreList
from application.resources.user import UserRegister
from application.security import authenticate, identity

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harsh:test@localhost:5432/udemy4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)