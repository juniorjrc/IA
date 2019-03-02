import tkinter as tk  #importa a biblioteca gráfica TKINTER
from pacotes.Desenho import *

class Mapa:
    def __init__(self, nome, altura, largura):
        self.nome 			= nome
        self.altura 		= altura
        self.largura 		= largura
        self.retangulo  	= makeRetangulos(altura, largura) #Objeto responsável pelos retangulos do mapa

    class Retangulo:
        def __init__(self, x, y, tipo, cor, estaOcupado, inimigo):
            self.x 				= x
            self.y 				= y
            self.tipo 			= tipo
            self.cor 			= cor
            self.estaOcupado 	= estaOcupado
            self.inimigo 		= inimigo


#Gera o mapa chamando a classe Mapa, que por padrão possui o objeto Retangulo, que compõe os retangulos no mapa
def makeMapa(nome, altura, largura):
    retangulo = Mapa(nome, altura, largura)
    return retangulo


#Gera os retangulos do mapa
def makeRetangulos(altura, largura):
    retangulos = [[Mapa.Retangulo(x, y, "Surface", "black", False, "None") for x in range(altura)] for y in range(largura)]
    return retangulos


#Preenche o mapa com as cores neutras
def preencheMapa(mapa, matriz, m1, m2):
    # Preenche os campos do objeto Mapa / Apenas preenche não desenha
    for x in range(m1):
        for y in range(m2):
            mapa.retangulo[x][y].cor = "gray"

    # Atribui o mapa a matriz 10x10
    #Preenche as colunas da matriz com a cor neutra
    for x in range(m1):
        #Preenche as linhas na matriz
        for y in range(m2):
            #if x >= len(elemento):
            matriz[x][y] = mapa.retangulo[x][y].cor

    # Insere a coloração dos elementos na matriz através da classe DESENHO
    setaElementosMapa(matriz, m1, m2)

    return matriz


#Desenha o mapa em tela através da biblioteca do canvas
def desenhaMapa(largura, altura, matriz):
    canvas                      = tk.Canvas(width=largura, height=altura)
    linhas, colunas             = len(matriz), len(matriz[0])
    ret_largura, ret_altura     = largura // linhas, altura // colunas

    for y, linha in enumerate(matriz):
        for x, color in enumerate(linha):
            x0, y0 = x * ret_largura, y * ret_altura
            x1, y1 = x0 + ret_largura - 1, y0 + ret_altura - 1
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    canvas.pack()