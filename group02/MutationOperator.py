import random
import numpy


class MutationOperator:

    @staticmethod
    def apply(lista,F=(random.random() * 2)):
        best = numpy.array(lista[0].vector)
        x1 = numpy.array(lista[1].vector)
        x2 = numpy.array(lista[2].vector)
        f=F

        # devuelve un vector mutado aplicando de/best/1
        return best + f * (x1 - x2)
