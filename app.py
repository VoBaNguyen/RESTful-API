import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://bnqhmmgtqpipvz:ddb1cb6065800ff330628a1672a3157f31e216690c931cfe82f54745a96357d1@ec2-34-193-101-0.compute-1.amazonaws.com:5432/dd1bou8v4fhlsd"
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # Turn of flask SQLAlchemy modification tracker
app.secret_key = "jose"
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")  # http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
