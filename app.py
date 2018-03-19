from bottle import run
from dao import UserDao

if __name__ == '__main__':
    UserDao(database='figurinhas')
    run(app='route', host='localhost', port=8080)
