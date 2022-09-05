from flask_restful import Resource, reqparse
from usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('userid',
                        type=int,
                        required=True,
                        help="Please input your userid")
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Please input your username")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Please input your password")

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message": "this user already exist"}, 400
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user created successfully"}, 201
