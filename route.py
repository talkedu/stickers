from bottle import get, post, response, request
from model import User, ModelEncoder
from json import dumps
from dao import UserDao


user_dao = UserDao()


@get('/users')
def get_all_users():
    response.content_type = 'application/json'
    users = user_dao.find_all()
    return dumps(users, cls=ModelEncoder)


@post('/users')
def create_user():
    user = User.from_dict(**request.json)
    user_dao.save(user)
    response.content_type = 'application/json'
    return dumps(user, cls=ModelEncoder)
