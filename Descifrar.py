import numpy


def descifrado(vector, args, final=False):
    for i in vector:
        i = int(i)
    desc = Descifrar()
    fitness = desc.f(vector, args[0], args[1])
    if final:
        print(desc.origtext)
    return fitness


class Descifrar:
    def __init__(self):
        self.origtext = ""

    def generateKey(self, string, key):
        # comprueba que la clave sea del tamaño del texto
        if len(string) <= len(key):
            return key
        # si no lo es, repite la clave hasta que lo sea
        else:
            for i in range(len(string) - len(key)):
                key = numpy.append(key, key[i % len(key)])
        return key

    def decipher(self, key, texto):
        orig_text = []
        for i in range(len(texto)):
            x = (ord(texto[i]) - (key[i] + 65) + 26) % 26
            x += ord('A')
            orig_text

            orig_text.append(chr(int(x)))
        return "".join(orig_text)

    def f(self, vector, texto, palabras):
        key = self.generateKey(texto, vector)
        orig_text = self.decipher(key, texto)
        self.origtext = orig_text
        fitness = 1
        coincidencias = 0

        for i in palabras:
            coincidencias = 1
            for k in range(len(orig_text)):
                aux = 0
                if len(i) <= len(orig_text) - k:
                    for j in range(len(i)):

                        if i[j] == orig_text[k + j]:
                            aux += 1
                    if aux > coincidencias:
                        coincidencias = aux
            fitness *= pow(coincidencias, 2)

            """aux =0
                for j in range(len(i)):
                    if i[j] == orig_text[k]:
                        fitness = fitness + aux
                        aux *= 20
                        if j == len(i) - 1:
                            aux2 = aux

                        if k + 1 < len(orig_text):
                            k += 1
                        else:
                            break
                    else:
                        aux = aux2"""

        return 1 / fitness
