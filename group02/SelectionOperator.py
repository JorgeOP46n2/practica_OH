import random
class SelectionOperator(object):

    def apply(self, population, target):
        selection = [population.list[target]]
        for i in range(3):
            aux = random.randint(0, len(population.list)-1)
            while aux == target:
                aux = random.randint(0, len(population.list)-1)
            selection.append(population.list[aux])
        return selection
