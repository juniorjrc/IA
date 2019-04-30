import tkinter as tk  #importa a biblioteca gráfica TKINTER
from pacotes import Desenho as d
from pacotes import Jogador as j 
from pacotes import Destino as dt
from pacotes import Ambiente as a
import pacotes.Busca as b
import pacotes.Grafo as g
li = 0
co = 0
class Mapa:
    def __init__(self, nome, altura, largura):
        self.nome 			= nome
        self.altura 		= altura
        self.largura 		= largura
        self.retangulo  	= makeRetangulos(altura, largura) #Objeto responsável pelos retangulos do mapa

    class Retangulo:
        def __init__(self, nome, x, y, tipo, cor, estaOcupado, inimigo):
            self.nome           = nome
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
    nome            = ""
    retangulos      = [[Mapa.Retangulo(nome, x, y, "Surface", "black", False, "None") for x in range(altura)] for y in range(largura)]
    return retangulos


#Preenche o mapa com as cores neutras
def preencheMapa(mapa, matriz, m1, m2):
    posicao = 1
    # Preenche os campos do objeto Mapa / Apenas preenche não desenha
    for x in range(m1):
        for y in range(m2):
            mapa.retangulo[x][y].nome   = posicao
            mapa.retangulo[x][y].cor    = "gray"
            posicao += 1

    # Atribui o mapa a matriz 6x6
    #Preenche as linhas da matriz com a cor neutra
    for x in range(m1):
        #Preenche as colunas na matriz
        for y in range(m2):
            #if x >= len(elemento):
            matriz[x][y] = mapa.retangulo[x][y].cor


    return matriz


#Desenha o mapa em tela através da biblioteca do canvas
def desenhaMapa(largura, altura, matriz, m1, m2):
    #======================================================================#
    # Insere a coloração dos elementos na matriz através da classe DESENHO #
    #         METÓDO PRINCIPAL DO DESENHO DOS ELEMENTOS NA MATRIZ          #
    #======================================================================#

    matrizAmbiente = d.setaElementosMapa(matriz, m1, m2)

    ambiente = a.Ambiente(matriz)
    matrizPesos = ambiente.geraMatrizPesos(matrizAmbiente)
    grafoPesos = g.grafoPesos(matriz, matrizPesos)

    canvas                      = tk.Canvas(width=largura, height=altura)
    linhas, colunas             = len(matriz), len(matriz[0])
    ret_largura, ret_altura     = largura // linhas, altura // colunas
    jogador                     = j.Jogador(m1, m2)
    destino                     = dt.Destino(m1, m2)
    lines, columns              = b.exec(g.nos(m1, m2), g.grafo(matriz), m1, m2, grafoPesos)
    canvas.pack()
    #Trecho inserido para testes de movimentação do jogador
    def movimentaJogador():
        posicao = 0
        global li
        global co
        if lines != [] and columns != []:
            for y, linha in enumerate(matriz):
                for x, color in enumerate(linha):
                    x0, y0          = x * ret_largura, y * ret_altura
                    x1, y1          = x0 + ret_largura - 1, y0 + ret_altura - 1
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
                    posicao         += 1
                    canvas.create_text(x0 + 21, y0 + 30, font=("Purisa", 40), text=posicao, fill="white")
                    canvas.create_text(x0 + 130, y0 + 30, font=("Purisa", 20), text=matrizPesos[y][x], fill="black")

                    if y == destino.linha and x == destino.coluna:
                        canvas.create_oval(x0, y0, x1, y1, fill=destino.cor, outline=color)
                        canvas.create_text((x0+x1)/2, (y0+y1)/2, font=("Purisa", 40), text="♚", fill="white")

                    # AQUI SERÃO REALIZADOS AS VALIDAÇÕES DE MOVIMENTAÇÃO DO JOGADOR
                    if y == int(lines[li]) and x == int(columns[co]):
                        canvas.create_oval(x0, y0, x1, y1, fill=jogador.cor, outline="")
                        canvas.create_text((x0+x1)/2, (y0+y1)/2, font=("Purisa", 40), text="☠", fill="white")
            li += 1
            co += 1
            if li < len(lines) and co < len(columns):
                canvas.after(1000, movimentaJogador)
            else:
                canvas.create_text(400, 300, font=("Purisa", 70),
                                   text="ENCONTROU!!!", fill="black")
        else:
            canvas.create_text(400, 300, font=("Purisa", 20), text="Não existe o caminho de acordo com o limite inserido", fill="black")
    movimentaJogador()
