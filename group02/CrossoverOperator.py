import random


class CrossoverOperator:


    @staticmethod
    def apply(lista):
        lista = lista
        CR = 0.6
        trialv = []
        i_rand = random.randint(0, len(lista.poblacion[0])-1)

        for j in range(len(lista.poblacion[0])):
            if j != i_rand and random.random() <= CR:
                trialv.append(lista.poblacion[0].vector[j])
            else:
                trialv.append(lista.poblacion[1].vector[j])
        return trialv
