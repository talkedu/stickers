from abc import abstractmethod
from pymongo import MongoClient
from model import User


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DAO(metaclass=Singleton):

    def __init__(self, database, username=None, password=None, host='localhost', port=27017):
        self.__username = username
        self.__password = password
        self.__client = MongoClient(host=host, port=port)
        self.__database = self.__client[database]

    @property
    def database(self):
        return self.__database

    @abstractmethod
    def collection(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def find_all(self):
        pass


class UserDao(DAO):

    @property
    def collection(self):
        return self.database['user']

    def save(self, user):
        return self.collection.insert_one(user.__dict__()).inserted_id

    def find_all(self):
        return [User.from_dict(**doc) for doc in self.collection.find()]

