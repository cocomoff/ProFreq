from item import UItem, Trans
from database import Database

class DBOp(object):
    def __init__(self):
        pass

    @staticmethod
    def expected_support(X, db):
        count = 0
        for t in db:
            if X <= t.itemset:
                prob = 1.0
                for itemX in X:
                    prob *= t.prob[itemX]
                count += prob
        return count


if __name__ == '__main__':
    db = Database.toy()
    db.dump()
    X1 = set({"D"})
    esX1 = DBOp.expected_support(X1, db)
    print(X1, esX1)

    X2 = set({"G"})
    esX2 = DBOp.expected_support(X1, db)
    print(X2, esX2)

