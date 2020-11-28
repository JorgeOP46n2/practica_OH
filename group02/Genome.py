#clase para almacenar vectores junto a su fitness
class Genome:
    def __init__(self, vector, f):
        self.vector = vector
        self.fitness = abs(f(vector))
