from tkinter import *  
from src.Retangulo import *
from src.Desenhista import *

class Mapa():

    def __init__(self, nome, altura, largura):
        self.nome = nome
        self.altura = altura
        self.largura = largura
        self.retangulo = Retangulo.make(altura, largura)
        #1°nome, 2°altura, 3°largura, 4° cria uma lista de objetos retangulos

    def parametrizar(mapa, matriz, L, C, elementos, jogador, destino):
        for x in range(L):
            for y in range(C):
                matriz[x][y] = mapa.retangulo[x][y].elemento
                #preenche a matriz igual o mapa(tudo solo)
                
        matriz = Desenhista.inserirElementos(matriz, L, C, elementos)
        #insere todos elementos definidos no Mapa.py
        
        matriz = Desenhista.inserirJogadoreDestino(matriz, L, C, jogador, destino)
        #insere o jogador e destino definidos no Mapa.py
        
        return matriz
        #retorna a matriz completa


