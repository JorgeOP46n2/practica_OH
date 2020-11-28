from group02.EA import EA
import numpy
from benchmarks import functions
import threading


def f(funcion, numero):



    mybounds = [(0, 1)] * 10

    myEA = EA(funcion, mybounds, 50)
    myEA.setCR(0.6)
    myEA.setF(1)

    myEA.run(500)

    bestGenome = myEA.best
    print("El fitness del thread "+str(numero)+" es: "+str(bestGenome.fitness))

if __name__ == "__main__":

    t1 = threading.Thread(target=f,kwargs={"numero": 1,"funcion":functions.ackley})
    t2 = threading.Thread(target=f, kwargs={"numero": 2, "funcion": functions.rastrigin})
    t3 = threading.Thread(target=f, kwargs={"numero": 3, "funcion": functions.rosenbrock})
    t4 = threading.Thread(target=f, kwargs={"numero": 4, "funcion": functions.schwefel_2_21})
    t5 = threading.Thread(target=f, kwargs={"numero": 5, "funcion": functions.schaffer})
    t6 = threading.Thread(target=f, kwargs={"numero": 6, "funcion": functions.griewank})
    threads=[t1,t2,t3,t4,t5,t6]
    for t in threads:
        t.start()
