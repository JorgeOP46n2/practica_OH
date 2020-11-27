from group02.Population import Population


class ReplacementOperator:
    def apply(self, pop1, pop2):
        replacedPop = Population()
        pop1.ordenar_ascendente()
        pop2.ordenar_ascendente()
        for i in range(len(pop1.lista)):
            if pop1.lista[i].fitness <= pop2.lista[i].fitness:
                replacedPop.add(pop1.lista[i])
            else:
                replacedPop.add(pop2.lista[i])
        return replacedPop
