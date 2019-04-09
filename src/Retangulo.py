from src.Elementos import *
class Retangulo():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = "Surface"
        self.elemento = Elementos.get()['solo']
        self.ocupado = False
        #1°pos x, 2°pos y, 3°tipo(não alterar),4°por padrão, tudo é solo
        #5°nada ocupado

    @staticmethod
    def make(altura, largura):
        retangulos = [[Retangulo(x,y) for x in range(altura)] for y in range(largura)]
        #dado a largura e altura, cria uma lista de objetos retangulos
        
        return retangulos
        #retorna a lista
        
