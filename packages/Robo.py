from random import randint
import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk
class Robo:
    def __init__(self, linha, coluna):
        self.linha      = defineLinha(linha)
        self.coluna     = defineColuna(coluna)
        self.cor        = defineCorRobo()
        self.imagem     = defineImagem()
        self.simbolo    = defineSimbolo()
        self.posicaoRobo = self.linha * linha + (self.coluna + 1)

def defineLinha(linha):
    #linhaJogador = randint(0, m1-1)
    linhaRobo = 4
    return linhaRobo

def defineColuna(coluna):
    #colunaJogador = randint(0, m2-1)
    colunaRobo = 4
    return colunaRobo

def defineCorRobo():
    corRobo = "gray"
    return corRobo

def defineImagem():
    batman = Image.open(r'./Images/batman.png')
    basewidth = 100
    bwpercent = (basewidth/ float(batman.size[0]))
    bhsize = int((float(batman.size[1]) * float(bwpercent)))
    batman = batman.resize((basewidth, bhsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(batman)

    return photo

def defineSimbolo():
    simbolo = Image.open(r'./Images/simbolo.png')
    basewidth = 600
    bwpercent = (basewidth/ float(simbolo.size[0]))
    bhsize = int((float(simbolo.size[1]) * float(bwpercent)))
    simbolo = simbolo.resize((basewidth, bhsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(simbolo)

    return photo