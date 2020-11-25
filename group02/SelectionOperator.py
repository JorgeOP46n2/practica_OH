import random


class SelectionOperator:
    @staticmethod
    def apply(population, target):
        selection = [population.poblacion[target]]
        for i in range(3):
            aux = random.randint(0, len(population.poblacion) - 1)
            while aux == target:
                aux = random.randint(0, len(population.poblacion) - 1)
            selection.append(population.poblacion[aux])
        return selection
