from group02.Population import Population
from group02.Genome import Genome
from group02.SelectionOperator import SelectionOperator
from group02.MutationOperator import MutationOperator
from group02.CrossoverOperator import CrossoverOperator
from group02.ReplacementOperator import ReplacementOperator
import numpy
import random


class EA(object):
    """docstring for EA"""

    def __init__(self, function, mybounds, number):
        # super(EA, self).__init__()
        self.function = function
        self.mybounds = mybounds
        self.number = number
        v_aux = []
        conjunto_x = []
        self.generation = []
        self.best = None

        # inizialization
        for i in range(number):
            mini = self.mybounds[0].__getitem__(0)
            maxi = self.mybounds[0].__getitem__(1)
            vector = mini + numpy.random.random_sample(len(self.mybounds)) * (maxi - mini)
            genoma = Genome(vector, self.function)
            conjunto_x.append(genoma)
        # se convierte el conjunto auxiliar en population
        init_Pop = Population(conjunto_x)
        init_Pop.ordenar_ascendente()
        self.best = init_Pop.lista[0]
        # se añade la population a la lista de generaciones
        self.generation.append(init_Pop)

    def run(self, iteraciones):
        i = 0
        while i < iteraciones and self.best.fitness != 0:
            # se ordena la lista de mejor a peor fitness
            self.generation[i].ordenar_ascendente()

            # se guarda el best en el atributo de EA
            self.best = self.generation[i].lista[0]
            print(self.best.vector)
            # crea la population de trials
            trialv_pop = Population()

            # por cada vector de la poblacion
            for j in range(len(self.generation[i].lista)):
                # crea un operador de seleccion al que se le pasa la poblacion actual y el indice del target
                mySelOp = SelectionOperator()

                # apply devuelve una lista con el target y dos aleatorios
                selection = mySelOp.apply(self.generation[i], j)

                # se le pasa selection a mutation
                myMutOp = MutationOperator()
                mutationVector = myMutOp.apply([self.best]+selection[1:3])
                g_mutation = Genome(mutationVector, self.function)
                pop_aux = Population([g_mutation, self.generation[i].lista[j]])

                # se crea el trial vector
                myCrossOp = CrossoverOperator()
                crossoverVector = myCrossOp.apply(pop_aux)
                g_crossover = Genome(crossoverVector, self.function)

                trialv_pop.add(g_crossover)
            # replacement
            myRepOp = ReplacementOperator()
            newPop = myRepOp.apply(trialv_pop, self.generation[i])
            self.generation.append(newPop)
            i = i + 1

    def best(self):
        return self.best()
