import random
import numpy
class MutationOperator(object):

    @staticmethod
    def apply(lista):
        best = lista[0].vector
        x1 = lista[1].vector
        x2 = lista[2].vector
        result = []
        for i in range(len(best)):
            result.append(best[i] + random.random() * (x1[i] - x2[1]))
        return result
