################################################
#       v4.0 - BATMAN NEEDS FIND JOKER         #
################################################
import tkinter as tk
from packages import Mapa as mapa
from packages import Desenho as d
from packages import Interface as i
desenho = d.Desenho()

#DEFINIÇÃO DE LINHAS E COLUNAS DO MAPA
linhas      = 5
colunas     = 5

#LARGURA E ALTURA DO MAPA
largura, altura = 800,600

#CRIAÇÃO DO MAPA E IMPLEMENTAÇÃO DA MATRIZ BASE DOS OBJETOS
mapa = mapa.Mapa("BATMAN VS JOKER", linhas, colunas)
matriz      = [[0 for x in range(linhas)] for y in range(colunas)]

#PREENCHE A MATRIZ COM OS ELEMENTOS(COR, PESO, NOME, ETC..)
mapaDesenhado = desenho.preencheMatriz(mapa, matriz, linhas, colunas)

#DESENHA O MAPA EM TELA
desenho.desenhaMapa(largura, altura, mapaDesenhado, linhas, colunas)



