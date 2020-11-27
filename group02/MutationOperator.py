import random
import numpy


class MutationOperator:

    @staticmethod
    def apply(lista):
        target = lista[0].vector
        x1 = lista[1].vector
        x2 = lista[2].vector

        return target + random.random() * (x1 - x2)
