# -*- coding: utf-8 -*-

class UItem(object):
    def __init__(self, key, prob):
        self.key = key
        self.prob = prob

    def Item(self):
        return self.key

    def P(self):
        return self.prob

    def __str__(self):
        return "({};{})".format(self.key, self.prob)


class Trans(object):
    def __init__(self, loui):
        self.loui = loui

    def __str__(self):
        ans = "["
        for uitem in self.loui:
            ans += str(uitem) + " "
        ans = ans[:-1] + "]"
        return ans

    def __iter__(self):
        return iter(self.loui)

    @staticmethod
    def build_from_list(loui):
        ans = []
        for (key, prob) in loui:
            ans.append(UItem(key, prob))
        return Trans(ans)
