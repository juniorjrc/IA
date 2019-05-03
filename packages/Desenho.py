#BIBLIOTECAS GRÁFICAS
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk

import packages.Busca as b
from packages import Grafo as g
from packages import Elementos as e
from packages import Robo as r
from packages import Destino as d
elmnts = e.Elementos()

elementos       = elmnts.elementos
tamanhoMaximo   = elmnts.tamanhoMaximo
cores           = elmnts.cores
pesos           = elmnts.pesos

li = 0
co = 0

class Desenho(): 
    #MÉTODO DE PREENCHIMENTO DA MATRIZ COM OS ATRIBUTOS ESPECIFICOS DE CADA RETANGULO   
    def preencheMatriz(self, mapa, matriz, linhas, colunas):
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                matriz[linha][coluna] = mapa.retangulo[linha][coluna]
        
        self.setaElementosMapa(matriz, linhas, colunas)

        return matriz
    
    #SETA OS ELEMENTOS NO MAPA
    def setaElementosMapa(self, matriz, linhas, colunas):
        contaCasas = 0
        contaCasasOcupadas = 0
        contaElemento = 0
        terminou = False
        valorElementos, listaElementos = self.defineValoresElementos(linhas, colunas)

        x = 0
        y = 0

        while x < linhas:
            while y < colunas:
                if terminou:
                    x = linhas
                    y = colunas
                    break
                x, y, linhas, colunas, matriz,\
                contaElemento, contaCasas, contaCasasOcupadas, listaElementos,\
                valorElementos, terminou = self.pintaBlocos(x, y, linhas, colunas, matriz, contaElemento, contaCasas, contaCasasOcupadas, listaElementos, valorElementos, terminou)

        return matriz
    
    #PINTA OS BLOCOS COM AS CORES
    def pintaBlocos(self, x, y, linhas, colunas, matriz, contaElemento, contaCasas, contaCasasOcupadas, listaElementos, valorElementos, terminou):
        if matriz[x][y].cor == "gray":
            matriz[x][y].elemento = elementos[contaElemento]
            matriz[x][y].cor = cores[0][elementos[contaElemento]]
            matriz[x][y].pesos = pesos[0][elementos[contaElemento]]
            contaCasas += 1
            contaCasasOcupadas += 1

            x, y, contaCasas = self.verificaUltimaColuna(x, y, colunas, contaCasas)

            x, y, terminou, contaCasas = self.verificaUltimaLinhaUltimaColuna(x, y, colunas, contaElemento, listaElementos, contaCasasOcupadas, valorElementos, contaCasas, terminou)

            x, contaCasas = self.verificaUltimaLinha(x, colunas, contaCasasOcupadas, valorElementos, listaElementos, contaElemento, contaCasas)

            x, y, contaCasas = self.verificaContaCasas(contaCasas, listaElementos, contaElemento, x, y)

            terminou, x, contaElemento, contaCasasOcupadas, contaCasas = self.verificaContaCasasOcupadas(contaCasasOcupadas, valorElementos, contaElemento, listaElementos, x, contaCasas, terminou)

        else:
            x, y, contaCasas = self.buscaBlocoNeutro(x, y, linhas, colunas, contaCasasOcupadas, valorElementos, contaElemento, contaCasas)
        
        return x, y, linhas, colunas, matriz, contaElemento, contaCasas, contaCasasOcupadas, listaElementos, valorElementos, terminou
    
    #VERIFICA ULTIMA COLUNA DE PREENCHIMENTO PARA NAO ESTOURAR O VETOR
    def verificaUltimaColuna(self, x, y, colunas, contaCasas):
        if y == colunas:
            x += 1
            y = 0
            contaCasas = 0
        
        return x, y, contaCasas
    
    #VERIFICA ULTIMA LINHA E ULTIMA COLUNA DE PREENCHIMENTO PARA NÃO ESTOURAR O VETOR
    def verificaUltimaLinhaUltimaColuna(self, x, y, colunas, contaElemento, listaElementos, contaCasasOcupadas, valorElementos, contaCasas, terminou):
        if x == colunas - 1 and y == colunas - 1:
            if contaElemento >= len(listaElementos) - 1:
                if contaCasasOcupadas <= valorElementos[contaElemento]:
                    x = 0
                    y = 0
                else:
                    terminou = True
            
            else:
                x -= 1
                y = 0
                contaCasas = 0
        return x, y, terminou, contaCasas
    
    #VERIFICA ULTIMA LINHA PARA NAO ESTOURAR O VETOR
    def verificaUltimaLinha(self, x, colunas, contaCasasOcupadas, valorElementos, listaElementos, contaElemento, contaCasas):
        if x == colunas - 1:
            if contaCasasOcupadas <= valorElementos[contaElemento]:
                if contaCasas <= tamanhoMaximo[0][listaElementos[contaElemento]]:
                    x = 0
                    contaCasas = 0
                else:
                    contaCasas = 0
            else:
                x -= 1
                contaCasas = 0
        
        return x, contaCasas
    
    def verificaContaCasas(self, contaCasas, listaElementos, contaElemento, x, y):
        if contaCasas == tamanhoMaximo[0][listaElementos[contaElemento]]:
            y -= y
            x += 1
            contaCasas = 0
        return x, y, contaCasas
    
    def verificaContaCasasOcupadas(self, contaCasasOcupadas, valorElementos, contaElemento, listaElementos, x, contaCasas, terminou):
        if contaCasasOcupadas >= valorElementos[contaElemento]:
            if contaElemento >= len(listaElementos) - 1:
                terminou = True
            else:
                x = 0
                contaElemento += 1
                contaCasasOcupadas = 0
                contaCasas = 0
        return terminou, x, contaElemento, contaCasasOcupadas, contaCasas

    def buscaBlocoNeutro(self, x, y, linhas, colunas, contaCasasOcupadas, valorElementos, contaElemento, contaCasas):
        y += 1
        if y == colunas:
            if y >= linhas - 1 and x >= colunas - 1 and contaCasasOcupadas <= valorElementos[contaElemento]:
                x = 0
                y = 0
            else:
                x += 1
                y = 0
                contaCasas = 0
        
        return x, y, contaCasas

    def defineValoresElementos(self, linha, coluna):
        listaElementos  = []  # Lista dos elementos
        valorElemento   = []  # valor das quantidades de cada elemento

        listaElementos = ["NORTH_ISLAND", "NARROWS", "TRICORNER_YARDS", "HAYSVILLE", "PARKVILLE", "SOUTH_ISLAND", "BLACK_GATE", "BRISTOL_HILLS"]
        self.corrigePosicaoElementos(listaElementos)

        valorElemento = [2, 3, 5, 4, 4, 1, 4, 2]

        return valorElemento, listaElementos

    #MÉTODO DE DESENHO DO MAPA EM INTERFACE GRÁFICA NA TELA
    def desenhaMapa(self, largura, altura, matriz, linhas, colunas):
        root    = tk.Tk()
        root.title("BATMAN NEED'S FIND JOKER")
        frame   = tk.Frame()
        frame.pack()
        canvas = tk.Canvas(width=largura, height=altura)

        linhas, colunas = len(matriz), len(matriz[0])
        ret_largura, ret_altura     = largura // linhas, altura // colunas
        batman = r.Robo(linhas, colunas)
        coringa = d.Destino(linhas, colunas)
        grafo = g.Grafo(matriz)
        lines, columns = b.exec(grafo.nos, grafo.grafo, linhas, colunas, grafo.grafoParametrizado, grafo.posicoes)
        canvas.pack()

        #MOVIMENTA O JOGADOR DE ACORDO COM OS ALGORITMOS DE BUSCA
        def movimentaJogador():
            posicao = 0
            global li
            global co

            if lines != [] and columns != []:
                for y, linha in enumerate(matriz):
                    for x, retangulo in enumerate(linha):
                        x0, y0          = x * ret_largura, y * ret_altura
                        x1, y1          = x0 + ret_largura - 1, y0 + ret_altura - 1
                        canvas.create_rectangle(x0, y0, x1, y1, fill=retangulo.cor, width=0)
                        posicao += 1
                        canvas.create_text(x0 + 60, y0 + 100, font=("Helvetica", 10), text=matriz[y][x].elemento, fill="white")
                        canvas.create_text(x0 + 31, y0 + 30, font=("Helvetica", 30), text=matriz[y][x].posicao, fill="#0B0B3B")
                        canvas.create_text(x0 + 130, y0 + 100, font=("Helvetica", 20), text=matriz[y][x].pesos, fill="white")

                        if y == coringa.linha and x == coringa.coluna:
                            canvas.create_image(x0 + 25, y0, image=coringa.imagem, anchor='nw')
                        
                        if y == int(lines[li]) and x == int(columns[co]):
                            canvas.create_image(x0 + 25, y0, image=batman.imagem, anchor='nw')
                li += 1
                co += 1
                if li < len(lines) and co < len(columns):
                    canvas.after(1000, movimentaJogador)
                else:
                    canvas.create_image(80, 100, image=batman.simbolo, anchor='nw')
                    canvas.create_text(400, 300, font=("Purisa", 20),
                                   text="O BATMAN ENCONTROU O CORINGA!!!", fill="white")
            else:
                canvas.create_text(400, 300, font=("Purisa", 20), text="NÃO FOI POSSÍVEL ENCONTRAR O CORINGA!!", fill="black")
        movimentaJogador()                  
        root.mainloop()
    
    #ORDENA OS ELEMENTOS DE ACORDO COM O INFORMADO
    def corrigePosicaoElementos(self, listaElementos):
        elementos.clear()
        for x, y in enumerate(listaElementos):
            elementos[x] = y

        return elementos
