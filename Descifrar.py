import numpy


def descifrado(vector, args, final=False):
    for i in vector:
        i = int(i)
    desc = args[0]
    fitness = desc.f(vector, )
    if final:
        print(desc.origtext)
    return fitness


class Descifrar:
    def __init__(self, texto, palabras):
        self.texto = texto
        self.origtext = ""
        self.palabras = palabras

    def generateKey(self, key):
        # comprueba que la clave sea del tamaño del texto
        if len(self.texto) <= len(key):
            return key
        # si no lo es, repite la clave hasta que lo sea
        else:
            for i in range(len(self.texto) - len(key)):
                key = numpy.append(key, key[i % len(key)])
        return key

    def decipher(self, key):
        orig_text = []
        for i in range(len(self.texto)):
            x = (ord(self.texto[i]) - (key[i] + 65) + 26) % 26
            x += ord('A')
            orig_text.append(chr(int(x)))
        return "".join(orig_text)

    def f(self, vector):
        key = self.generateKey(vector)
        orig_text = self.decipher(key)
        self.origtext = orig_text
        fitness = 1

        for i in self.palabras:
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
