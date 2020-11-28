from group02.Population import Population


class ReplacementOperator:
    @staticmethod
    def apply(pop1, pop2):
        replacedPop = Population()
        for i in range(len(pop1.lista)):
            # Compara el fitness del trial con el del target
            if pop1.lista[i].fitness <= pop2.lista[i].fitness:
                # si el fitness del trial es mejor que el del target, añade el trial a la poblacion
                replacedPop.add(pop1.lista[i])
            else:
                # si no, añade el target
                replacedPop.add(pop2.lista[i])
        return replacedPop
