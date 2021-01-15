import random
from group02.Population import Population


class SelectionOperator(object):

    @staticmethod
    def apply(population, target):
        selection = Population()
        # se selecciona el indice del vector aleatorio
        aux = random.randint(0, len(population.lista) - 1)
        selection.add(population.lista[aux])

        aux2 = random.randint(0, len(population.lista) - 1)
        while target == aux:
            aux = random.randint(0, len(population.lista) - 1)


        while aux == aux2 or target == aux2:
            aux2 = random.randint(0, len(population.lista) - 1)
        selection.add(population.lista[aux2])

        aux3 = random.randint(0, len(population.lista) - 1)
        while aux == aux3 or aux2 == aux3 or target == aux3:
            aux3 = random.randint(0, len(population.lista) - 1)
        selection.add(population.lista[aux3])

        return selection
