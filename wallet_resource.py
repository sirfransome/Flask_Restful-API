from flask_restful import Resource
from flask_jwt import jwt_required
from wallet_model import WalletModel
import json


class WalletName(Resource):  # class resource for crud operations


    @jwt_required()  # authentication token for users
    def get(self, client_name):
        wallet = WalletModel.find_by_name(client_name)
        if wallet:
            return json.dumps([x.json() for x in wallet], default=str)
        return {'message': 'wallet not found'}, 404

    @jwt_required()
    def delete(self, client_name):
        wallet = WalletModel.find_by_name(client_name)
        if wallet:
            wallet.delete_from_db()
        return {'message': 'wallet successfully deleted'}



class WalletAccountNumber(Resource):  # class item to retrieve all items from the table

    @jwt_required()  # authentication token for users
    def get(self, account_no):
        wallet = WalletModel.find_by_accountno(account_no)
        if wallet:
            return json.dumps([x.json() for x in wallet], default=str)
        return {'message': 'wallet not found'}, 404

    @jwt_required()
    def delete(self, account_no):
        wallet = WalletModel.find_by_accountno(account_no)
        if wallet:
            wallet.delete_from_db()
        return {'message': 'wallet successfully deleted'}