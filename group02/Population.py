def merge_sort(lista):
    if len(lista) < 2:
        return lista

    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)


def merge(lista1, lista2):
    i, j = 0, 0  # Variables de incremento
    result = []  # Lista de resultado

    # Intercalar ordenadamente
    while i < len(lista1) and j < len(lista2):
        if lista1[i].fitness < lista2[j].fitness:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result


class Population:
    def __init__(self, lista=None):
        if lista is None:
            lista = []
        self.poblacion = lista

    def ordenar_ascendente(self):
        self.poblacion = merge_sort(self.poblacion)

    def ordenar_descendente(self):
        self.poblacion = merge_sort(self.poblacion)
        self.poblacion.reverse()

    def add(self, solucion):
        self.poblacion.append(solucion)

    def remove(self, solucion):
        return self.poblacion.remove(solucion)

    def change(self, solucion1, solucion2):
        self.poblacion.remove(solucion1)
        return  self.poblacion.append(solucion2)
