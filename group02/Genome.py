# clase para almacenar vectores junto a su fitness
class Genome:
    def __init__(self, vector, f, args):
        self.vector = vector
        if args is not None:
            self.fitness = abs(f(vector, args))
        else:
            self.fitness = abs(f(vector))
