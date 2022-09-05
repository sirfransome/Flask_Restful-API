from db import db

class UserModel(db.Model):  # creates mapping between database and objects
    __tablename__ = 'users_table'  # name of table

    userid = db.Column(db.Integer, primary_key=True)  # columns in our table
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, userid, username, password):
        self.userid = userid
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.filter_by(userid=userid)
