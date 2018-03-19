from json import JSONEncoder
from bson import ObjectId


class ModelEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, Model):
                return o.__dict__()
            if isinstance(o, ObjectId):
                return str(o)
            return o


class Model:
    pass


class User(Model):

    def __init__(self, name, _id=None, stickers=None):
        self.__id = _id
        self.__name = name
        if stickers is None:
            self.__stickers = Sticker.blank_album()
        else:
            self.__stickers = stickers

    @staticmethod
    def from_dict(**d):
        return User(**d)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def stickers(self):
        return self.__stickers

    def add_sticker(self, number):
        self.__stickers[number] += 1

    def repeated(self):
        return {k: v for k, v in self.__stickers.items() if self.__stickers[k] > 1}

    def missing(self):
        return [k for k, v in self.__stickers.items() if self.stickers[k] == 0]

    def __dict__(self):
        return {
            'name': self.name,
            'stickers': self.stickers
        }


class Sticker(Model):

    def __init__(self, number, name=None):
        self.__number = number
        self.__name = name

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @staticmethod
    def blank_album():
        return {str(i + 1): 0 for i in range(0, 681)}

    def __eq__(self, other):
        return self.__number == other.__number

    def __hash__(self):
        return hash((self.number, self.name))

    def __repr__(self):
        return 'number={} name={}'.format(self.__number, self.__name)

