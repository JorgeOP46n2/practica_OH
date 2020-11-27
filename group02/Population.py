def merge_sort(list):
    if len(list) < 2:
        return list

    # De lo contrario, se divide en 2
    else:
        middle = len(list) // 2
        right = merge_sort(list[:middle])
        left = merge_sort(list[middle:])
        return merge(right, left)


def merge(list1, list2):
    i, j = 0, 0  # Variables de incremento
    result = []  # list de resultado

    # Intercalar ordenadamente
    while i < len(list1) and j < len(list2):
        if list1[i].fitness < list2[j].fitness:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result += list1[i:]
    result += list2[j:]

    # Retornamos el resultados
    return result


class Population:
    def __init__(self, list=None):
        if list is None:
            list = []
        self.list = list

    def ordenar_ascendente(self):
        self.list = merge_sort(self.list)

    def ordenar_descendente(self):
        self.list = merge_sort(self.list)
        self.list.reverse()

    def add(self, solution):
        self.list.append(solution)

    def remove(self, solution):
        return self.list.remove(solution)

    def change(self, solution1, solution2):
        self.list.remove(solution1)
        return  self.list.append(solution2)