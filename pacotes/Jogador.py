from random import randint

class Jogador:
    def __init__(self, m1, m2):
        self.m1         = m1
        self.m2         = m2
        self.linha      = defineLinha(self.m1)
        self.coluna     = defineColuna(self.m2)
        self.cor        = defineCorJogador()

def defineLinha(m1):
    linhaJogador =9
    return linhaJogador

def defineColuna(m2):
    colunaJogador = 7
    return colunaJogador

def defineCorJogador():
    corJogador = "gray"
    return corJogador