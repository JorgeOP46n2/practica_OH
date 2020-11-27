from group02.EA import EA
import group02.CrossoverOperator
import numpy
from benchmarks import functions


def f(sol):
    return sum(sol)


mybounds = [(0, 1)] * 10

myEA = EA(functions.rastrigin, mybounds, 50)
myEA.setCR(0.6)

myEA.run(1000)

bestGenome = myEA.best
print(bestGenome.fitness)

"""if __name__ == "__main__":
    print(mybounds[0].__getitem__(1))
    print(4+ numpy.random.random_sample(len(mybounds))*(6-4))
"""
