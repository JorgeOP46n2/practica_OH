import random
import numpy

class CrossoverOperator:
    def __init__(self, CR=0.5):
        self.CR = CR
        self.trialv = []

    def apply(self, population):
        # crea el valor Irand
        Irand = random.randint(0, len(population.lista[0].vector) - 1)

        for j in range(len(population.lista[0].vector)):

            # si no esta evaluando el gen con indice Irand y se cumple que el random es menor que CR
            if j != Irand and random.random() <= self.CR:

                # se hereda el gen del mutado
                self.trialv.append(population.lista[0].vector[j])
            else:

                #si se evalua el indice Irand o el random es mayor que CR se hereda el gen del target
                self.trialv.append(population.lista[1].vector[j])
        return self.trialv
