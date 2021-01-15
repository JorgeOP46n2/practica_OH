import random
import numpy


class CrossoverOperator:
    def __init__(self, CR=0.5):
        self.CR = CR
        self.trialv = []

    def apply(self, population):
        # crea el valor Irand
        longitud = len(population.lista[0].vector)
        n = random.randint(0, longitud - 1)
        L = 0
        while random.random() <= self.CR and (L <= longitud - 1):
            L += 1

        for j in range(len(population.lista[0].vector)):

            if j in range(n % longitud, (n + L) % longitud):
                self.trialv.append(population.lista[0].vector[j])
            else:
                self.trialv.append(population.lista[1].vector[j])
        return self.trialv
