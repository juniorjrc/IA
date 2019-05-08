from random import randint
import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk
class Robo:
    def __init__(self, linha, coluna):
        self.linha      = defineLinha(linha, coluna)
        self.coluna     = defineColuna(linha, coluna)
        self.cor        = defineCorRobo()
        self.imagem     = defineImagem()
        self.simbolo    = defineSimbolo()
        self.posicaoRobo = self.linha * linha + (self.coluna + 1)

def defineLinha(linha, coluna):
    p = 1
    linhaRobo = 0
    arqR = open("Files/batman.txt", "r+")
    posicao = arqR.read()
    arqR.close()

    for l in range(linha):
        for c in range(coluna):
            if p == int(posicao):
                linhaRobo = l
                
            p += 1

    return int(linhaRobo)

def defineColuna(linha, coluna):
    p = 1
    colunaRobo = 0
    arqR = open("Files/batman.txt", "r+")
    posicao = arqR.read()
    arqR.close()

    for l in range(linha):
        for c in range(coluna):
            if p == int(posicao):
                colunaRobo = c
                
            p += 1

    return int(colunaRobo)

def defineCorRobo():
    corRobo = "gray"
    return corRobo

def defineImagem():
    batman = Image.open(r'./Images/batman2.png')
    basewidth = 100
    bwpercent = (basewidth/ float(batman.size[0]))
    bhsize = int((float(batman.size[1]) * float(bwpercent)))
    batman = batman.resize((basewidth, bhsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(batman)

    return photo

def defineSimbolo():
    simbolo = Image.open(r'./Images/simbolo.png')
    basewidth = 200
    bwpercent = (basewidth/ float(simbolo.size[0]))
    bhsize = int((float(simbolo.size[1]) * float(bwpercent)))
    simbolo = simbolo.resize((basewidth, bhsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(simbolo)

    return photo