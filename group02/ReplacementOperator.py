from group02.Population import Population


class ReplacementOperator:
    def apply(self, pop1, pop2):
        replacedPop = Population()
        pop1.oredenar_ascendente()
        pop2.ordenar_ascendente()
        for i in range(len(pop1.list)):
            if pop1.list[i].fitness <= pop2.list[i].fitness:
                replacedPop.add(pop1.list[i])
            else:
                replacedPop.add(pop2.list[i])
        return replacedPop
