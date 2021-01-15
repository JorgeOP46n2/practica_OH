from group02.EA import EA
import numpy
import scipy.stats
import scipy.optimize
from group02.Genome import Genome
from benchmarks import functions
import threading
import Descifrar

data1 = []
data2 = []
vectores1 = []
vectores2 = []


def f(funcion, numero, bench, *args):
    mybounds = [(0, 24)] * 10
    if bench:

        returneo = scipy.optimize.differential_evolution(funcion, mybounds, None, "rand1exp", 50, 50, 0, 1, 0.6,
                                                         None, None, False, False, 'random', 0, 'deferred', 1)

        bestGenome = Genome(returneo.__getitem__("x"), funcion)
        global data2
        data2.append(bestGenome.fitness)
        vectores2.append(bestGenome.vector)

    else:
        myEA = EA(funcion, mybounds, 50, args)
        myEA.setCR(0.6)
        myEA.setF(1)
        myEA.run(1000)

        bestGenome = myEA.best
        global data1
        data1.append(bestGenome.fitness)
        vectores1.append(bestGenome.vector)
        print("El fitness del thread " + str(numero) + " es: " + str(1 / bestGenome.fitness))
        print("El resultado es:" + str(bestGenome.vector))
        funcion(bestGenome.vector, args, True)


if __name__ == "__main__":
    f(Descifrar.descifrado, 100, False,
      "HZAHEOMICEVMEWFBTVKGWKAMLSTVUXEMZNPEZKLMYVMMDUEVXQFMZMZLCICESTHYCAR",
      ["PRONTO", "KRIS", "DESCUBRE"])

    """ medias1 = []
    medias2 = []

    funciones = [functions.sphere, functions.ackley, functions.rosenbrock, functions.rastrigin, functions.griewank,
                 functions.schwefel_1_2, functions.schwefel_2_21, functions.schwefel_2_22, functions.extended_f_10,
                 functions.bohachevsky, functions.schaffer]
    todos1 = []
    todos2 = []
    for fun in funciones:
        for i in range(10):
            t1 = threading.Thread(target=f, kwargs={"numero": 1, "funcion": fun, "bench": False})

            t2 = threading.Thread(target=f, kwargs={"numero": 2, "funcion": fun, "bench": True})
            threads = [t1, t2]

            for t in threads:
                t.start()
            for t in threads:
                t.join()

        media1 = numpy.average(data1)
        stat, p = scipy.stats.friedmanchisquare(vectores1[0], vectores1[1], vectores1[2], vectores1[3], vectores1[4],
                                                vectores1[5], vectores1[6])
        print('RESULTADOS FRIEDMAN 1 \nStatistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
            print('Same distributions (fail to reject H0)')
        else:
            print('Different distributions (reject H0)')

        stat, p = scipy.stats.friedmanchisquare(vectores2[0], vectores2[1], vectores2[2], vectores2[3],
                                                vectores2[4], vectores2[5], vectores2[6])
        print('RESULTADOS FRIEDMAN 2 : \nStatistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
            print('Same distributions (fail to reject H0)')
        else:
            print('Different distributions (reject H0)')
        todos1.append(data1.copy())
        todos2.append(data2.copy())
        media2 = numpy.average(data2)
        vectores1 = []
        vectores2 = []
        data1 = []
        data2 = []
        print("La media de nuestra implementacion es: " + str(media1))
        print("La media de la importada  es: " + str(media2))
        medias2.append(media2)
        medias1.append(media1)"""
