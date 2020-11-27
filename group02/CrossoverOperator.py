import random
import numpy

class CrossoverOperator(object):
    def __init__(self, ):
        self.CR = 0.5
        self.trialv = []

    def apply(self, population):
        Irand = random.randint(0, len(population.lista[0].vector) - 1)
        for j in range(len(population.lista[0].vector)):

            if j != Irand and random.random() <= self.CR:
                self.trialv.append(population.lista[0].vector[j])
            else:
                self.trialv.append(population.lista[1].vector[j])
        return self.trialv
