from item import UItem, Trans
from database import Database

class DBOp(object):
    def __init__(self):
        pass

    @staticmethod
    def expected_support(X, db):
        pass


if __name__ == '__main__':
    db = Database.toy()
    db.dump()

