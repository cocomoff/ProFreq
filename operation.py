from item import UItem, Trans
from database import Database
from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt

class DBOp(object):
    def __init__(self):
        pass

    @staticmethod
    def prob_trans(X, t):
        prob = 1.0
        for itemX in X:
            if itemX in t.prob:
                prob *= t.prob[itemX]
            else:
                prob *= 0.0
                break
        return prob

    @staticmethod
    def expected_support(X, db):
        count = 0
        for t in db:
            if X <= t.itemset:
                count += DBOp.prob_trans(X, t)
        return count

    @staticmethod
    def support_probability(X, db, i):
        lT = len(db)
        all_prob = 0.0
        for comb in combinations(range(lT), i):
            prob = 1.0
            S = set(comb)
            nonS = set(range(lT)) - S
            for t in S:
                prob *= DBOp.prob_trans(X, db[t])
            for t in nonS:
                prob *= (1 - DBOp.prob_trans(X, db[t]))
            all_prob += prob
        return all_prob

    @staticmethod
    def frequentness(X, db, i, prob_dist=None):
        if prob_dist is None:
            prob_dist = []
            for j in range(len(db)+1):
                spX1i = DBOp.support_probability(X1, db, j)
                prob_dist.append(spX1i)
        answer = 0.0
        for j in range(i, len(db)+1):
            answer += prob_dist[j]
        return answer

    @staticmethod
    def frequentnessL10(X, db, i):
        lT = len(db)
        body = set(range(lT))
        all_prob = 1.0
        for ssize in range(i):
            for comb in combinations(range(lT), ssize):
                prob = 1.0
                S = set(comb)
                nonS = body - S
                for t in S:
                    prob *= DBOp.prob_trans(X, db[t])
                for t in nonS:
                    prob *= (1 - DBOp.prob_trans(X, db[t]))
                all_prob -= prob
        return all_prob

    @staticmethod
    def P(X, db, minsup):
        lT = len(db)
        mat = np.zeros((minsup+1, lT+1))
        mat[0, :] = 1
        for i in range(minsup+1):
            for j in range(lT+1):
                if i > j + 1:
                    mat[i, j] = np.nan

        # DP
        # P_{>=i,j} = P_{>=i-1,j-1} P(X in tj) + P_{>=i,j-1} (1 - P(X in tj))
        for i in range(1, minsup+1):
            for j in range(lT):
                Pxtj = DBOp.prob_trans(X, db[j])
                mat[i, j] = mat[i-1, j-1] * Pxtj + mat[i, j-1] * (1 - Pxtj)
                # print("DP @ i={},   j={}: {}".format(i, j, mat[i, j]))
                # print("   i-1={}, j-1={}: {}".format(i-1, j-1, mat[i-1, j-1]))
                # print("     i={}, j-1={}: {}".format(i, j-1, mat[i, j-1]))
                # print("   # {}".format(Pxtj))
        return mat[:, lT - 1]

    
def sample_expected_support():
    db = Database.toy()
    db.dump()
    X1 = set({"D"})
    esX1 = DBOp.expected_support(X1, db)
    print(X1, esX1)

    X2 = set({"G"})
    esX2 = DBOp.expected_support(X1, db)
    print(X2, esX2)

    
def sample_support_probability():
    db = Database.toy()
    db.dump()
    X1 = set({"D"})
    prob_dist = []
    for i in range(len(db)+1):
        spX1i = DBOp.support_probability(X1, db, i)
        prob_dist.append(spX1i)
    plt.plot(range(len(db)+1), prob_dist, "ro")
    plt.show()


def frequentness():
    db = Database.toy()
    db.dump()
    X1 = set({"D"})
    prob_dist = []
    for i in range(len(db)+1):
        spX1i = DBOp.support_probability(X1, db, i)
        prob_dist.append(spX1i)

    # frequentness
    freq_dist = []
    freq_distL10 = []
    for i in range(len(db)+1):
        fX1i = DBOp.frequentness(X1, db, i, prob_dist)
        fX1iL10 = DBOp.frequentnessL10(X1, db, i)
        freq_dist.append(fX1i)
        freq_distL10.append(fX1iL10)
    print(freq_dist)
    print(freq_distL10)
    # plt.plot(range(len(db)+1), freq_dist, "ro--")
    # plt.show()
    
if __name__ == '__main__':
    db = Database.toy()
    db.dump()
    X1 = set({"D"})

    freq_distL10 = []
    for i in range(len(db)+1):
        fX1iL10 = DBOp.frequentnessL10(X1, db, i)
        freq_distL10.append(fX1iL10)
    print(freq_distL10)

    vec = DBOp.P(X1, db, minsup=6)
    print(vec)
