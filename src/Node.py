
class Node:
    
    def __init__(self,value, proximo, anterior, pai,nivel):
        self.pai =  pai
        self.valor = value
        self.proximo = proximo
        self.anterior = anterior
        self.nivel = nivel

    
    def setNivel(self, nivel):
        self.nivel = nivel
