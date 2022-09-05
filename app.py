from datetime import timedelta
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from userresource import UserRegister
from wallet_resource import WalletName, WalletAccountNumber

# flask jwt helps to encode and decode basically for authentication

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://user:password@server_name.amazonaws.com:port/database'  # read the database
app.secret_key = '********'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # new end point /auth

api.add_resource(WalletName, "/walletname/<string:client_name>")
api.add_resource(WalletAccountNumber,
                 '/walletaccountno/<string:account_no>')  # the name variables goes into the parameter passed into the get method
api.add_resource(UserRegister, "/register")

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)  # debug keyword helps to get a better error message
