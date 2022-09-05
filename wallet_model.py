# create a new item model
from db import db  # handles all the connection to the database
from flask import request


class WalletModel(db.Model):
    __tablename__ = 'dwh_wallet_customers_account_statements'

    transaction_id = db.Column(db.Integer, primary_key=True)  # properties of our table
    transaction_date = db.Column(db.DateTime)
    account_no = db.Column(db.String(80))
    product = db.Column(db.String(80))
    client_name = db.Column(db.String(256))
    transaction_type = db.Column(db.String(80))
    debit = db.Column(db.Float(precision=2))
    credit = db.Column(db.Float(precision=2))
    balance = db.Column(db.Float(precision=2))
    reversed = db.Column(db.String(80))
    narration = db.Column(db.String(256))

    def __init__(self, transaction_id, transaction_date, account_no, product, client_name, transaction_type, debit,
                 credit, balance, reversed, narration):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.account_no = account_no
        self.product = product
        self.client_name = client_name
        self.transaction_type = transaction_type
        self.debit = debit
        self.credit = credit
        self.balance = balance
        self.reversed = reversed
        self.narration = narration

    def json(self):
        return {'transaction_id': self.transaction_id,
                'transaction_date': self.transaction_date,
                'account_no': self.account_no,
                'product': self.product,
                'client_name': self.client_name,
                'transaction_type': self.transaction_type,
                'debit': self.debit,
                'credit': self.credit,
                'balance': self.balance,
                'reversed': self.reversed,
                'narration': self.narration
                }

    @classmethod
    def find_by_name(cls, client_name):  # a class method to check if an item already exists on the database
        frm = request.args.get('from')
        to = request.args.get('to')
        return cls.query.filter_by(client_name=client_name).filter(cls.transaction_date >= frm).filter(
            cls.transaction_date <= to).all()  # select * from items where name=name .filter_by(date=data['date']

    @classmethod
    def find_by_accountno(cls, account_no):
        frm = request.args.get('from')
        to = request.args.get('to')
        return cls.query.filter_by(account_no=account_no).filter(cls.transaction_date >= frm).filter(
            cls.transaction_date <= to).all()

    def save_to_db(self):  # takes an item with a name and price
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
