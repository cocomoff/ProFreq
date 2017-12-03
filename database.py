# -*- coding: utf-8 -*-

from item import Trans

class Database(object):
    def __init__(self, transactions):
        self.transactions = transactions

    def __len__(self):
        return len(self.transactions)

    def __iter__(self):
        return iter(self.transactions)

    def dump(self):
        print("--------------")
        for trans in self.transactions:
            # print(trans.itemset)
            print(trans)
        print("--------------\n")


    @staticmethod
    def toy():
        toylist = [
            [("A", 1.0), ("B", 0.2), ("D", 0.5), ("F", 1.0)],
            [("B", 0.1), ("C", 0.7), ("D", 1.0), ("E", 1.0), ("G", 0.1)],
            [("A", 0.5), ("D", 0.2), ("F", 0.5), ("G", 1.0)],
            [("D", 0.8), ("E", 0.2), ("G", 0.9)],
            [("C", 1.0), ("D", 0.5), ("F", 0.8), ("G", 1.0)],
            [("A", 1.0), ("B", 0.2), ("C", 0.1)]
        ]
        ans = []
        for tlist in toylist:
            ans.append(Trans.build_from_list(tlist))
        return Database(ans)


if __name__ == '__main__':
    db = Database.toy()
    db.dump()
