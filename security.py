from usermodel import UserModel
import hmac


# authentication function takes username and password and select the correct user from our users
def authenticate(email, password):
    user = UserModel.find_by_username(email)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):  # payload is the content of the jwt token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
