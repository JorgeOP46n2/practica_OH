import random


class SelectionOperator(object):

    @staticmethod
    def apply(population, target):
        selection = [population.lista[target]]
        for i in range(2):
            aux = random.randint(0, len(population.lista) - 1)
            while aux == target:
                aux = random.randint(0, len(population.lista) - 1)
            selection.append(population.lista[aux])
        return selection
