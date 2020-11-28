import random
from group02.Population import Population

class SelectionOperator(object):

    @staticmethod
    def apply(population, target):

        #se añade el target a la lista a devolver
        selection = Population([population.lista[target]])



        #se selecciona el indice del vector aleatorio
        aux = random.randint(0, len(population.lista) - 1)
        #en el caso de que el indice aleatorio sea el del target, selecciona otro indice
        while aux == target:
            aux = random.randint(0, len(population.lista) - 1)

        #se añade el vector aleatorio
        selection.add(population.lista[aux])

        aux2=random.randint(0,len(population.lista)-1)
        while aux2 == target or aux == aux2:
            aux2 = random.randint(0, len(population.lista) - 1)
        selection.add(population.lista[aux2])
        return selection
