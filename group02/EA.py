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
        conjunto_x = []
        self.generation = []
        self.best = None
        self.CR = 0.5
        self.F=1

        # INITIALIZATION
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
        #contador de iteraciones
        i = 0
        while i < iteraciones and self.best.fitness != 0:
            # se ordena la lista de mejor a peor fitness
            # se guarda el best en el atributo de EA
            self.best = self.generation[i].ordenar_ascendente()[0]
            # print(Population(self.generation[i].ordenar_ascendente()).fitlist())
            # crea la population de trials
            trialv_pop = Population()

            # por cada vector de la poblacion
            for j in range(len(self.generation[i].lista)):
            #SELECTION
                mySelOp = SelectionOperator()

                # apply devuelve una lista con el target y dos aleatorios a partir de la poblacion actual y el indice del target
                selection = mySelOp.apply(self.generation[i], j)

            #MUTATION
                myMutOp = MutationOperator()

                # apply crea el vector de mutación aplicando de/best/1 a partir del best y dos donors (best + los 2 donors de selection)
                mutationVector = myMutOp.apply([self.best] + selection.lista[1:3],self.F)
                g_mutation = Genome(mutationVector, self.function)

                #  se crea una poblacion auxiliar con el genoma mutado y el genoma del target
                pop_aux = Population([g_mutation, self.generation[i].lista[j]])

            #CROSSOVER
                myCrossOp = CrossoverOperator(self.CR)

                # apply crea el trial vector aplicando binomial con probabilidad CR a partir del vector mutado y el target (pop_aux)
                crossoverVector = myCrossOp.apply(pop_aux)
                g_crossover = Genome(crossoverVector, self.function)

                # se añade el trial a una poblacion auxiliar
                trialv_pop.add(g_crossover)

        #REPLACEMENT
            myRepOp = ReplacementOperator()

            # apply devuelve una poblacion con los vectores reemplazados por su trial vector en el caso de que el trial vector tuviese mejor fitness que el target
            newPop = myRepOp.apply(trialv_pop, self.generation[i])

            #se añade la nueva población a la lista de generaciones
            self.generation.append(newPop)

            #se incrementa el contador de iteraciones
            i = i + 1

    #metodo que devuelve el mejor genoma
    def best(self):
        return self.best()

    #metodo que pasa un valor de CR para el crossover binomial (opcional)
    def setCR(self, valor):
        self.CR = valor

    def setF(self,valor):
        self.F=valor