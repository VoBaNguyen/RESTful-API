from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # Turn of flask SQLAlchemy modification tracker
app.secret_key = "jose"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")  # http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

db.init_app(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
