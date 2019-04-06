
class Node:
    
    def __init__(self,value, proximo, anterior, pai):
        self.pai =  pai
        self.valor = value
        self.proximo = proximo
        self.anterior = anterior
