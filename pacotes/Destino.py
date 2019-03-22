from random import randint

class Destino:
    def __init__(self, m1, m2):
        self.m1         = m1
        self.m2         = m2
        self.linha      = defineLinha(self.m1)
        self.coluna     = defineColuna(self.m2)
        self.cor        = defineCorDestino()

def defineLinha(m1):
    linhaDestino = 2
    return linhaDestino

def defineColuna(m2):
    colunaDestino = 3
    return colunaDestino

def defineCorDestino():
    corDestino = "red"
    return corDestino