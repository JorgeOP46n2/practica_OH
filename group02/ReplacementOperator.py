from group02.Population import Population


class ReplacementOperator:
    @staticmethod
    def apply(poblacion1, poblacion2):
        poblacionres = Population()
        poblacion1.ordenar_ascendente()
        for i in range(len(poblacion1.poblacion)):
            if poblacion1.poblacion[i].fitness > poblacion2.poblacion[i].fitness:
                poblacionres.add(poblacion1.poblacion[i])

            else:
                poblacionres.add(poblacion2.poblacion[i])

        return poblacionres
