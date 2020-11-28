import random
import numpy


class MutationOperator:

    @staticmethod
    def apply(lista):
        best = numpy.array(lista[0].vector)
        x1 = numpy.array(lista[1].vector)
        x2 = numpy.array(lista[2].vector)

        #devuelve un vector mutado aplicando de/best/1
        return best + (random.random()*2) * (x1 - x2)
