class Genome:
    def __init__(self, vector, f):
        self.vector = vector
        self.fitness = f(vector)
