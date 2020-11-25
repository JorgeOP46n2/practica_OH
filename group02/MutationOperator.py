import random


class MutationOperator(object):

    @staticmethod
    def apply(lista):
        best = lista[0]
        x1 = lista[1]
        x2 = lista[2]
        return best + random.random() * (x1 - x2)
