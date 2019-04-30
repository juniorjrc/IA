from random import randint

class Destino:
    def __init__(self, m1, m2):
        self.m1         = m1
        self.m2         = m2
        self.linha      = defineLinha()
        self.coluna     = defineColuna()
        self.cor        = defineCorDestino()
        self.posicaoDestino = self.linha * m1 + (self.coluna + 1)

def defineLinha():
    linhaDestino = 0
    return linhaDestino

def defineColuna():
    colunaDestino = 0
    return colunaDestino

def defineCorDestino():
    corDestino = "red"
    return corDestino