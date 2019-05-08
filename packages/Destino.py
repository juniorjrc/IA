from random import randint
import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

class Destino:
    def __init__(self, linha, coluna):
        self.linha      = defineLinha(linha, coluna)
        self.coluna     = defineColuna(linha, coluna)
        self.cor        = defineCorDestino()
        self.imagem     = defineImagem()
        self.posicaoDestino = self.linha * linha + (self.coluna + 1)

def defineLinha(linha, coluna):
    p = 1
    linhaDestino = 0
    arqR = open("Files/coringa.txt", "r+")
    posicao = arqR.read()
    arqR.close()

    for l in range(linha):
        for c in range(coluna):
            if p == int(posicao):
                linhaDestino = l
                
            p += 1

    return int(linhaDestino)

def defineColuna(linha, coluna):
    p = 1
    colunaDestino = 0
    arqR = open("Files/coringa.txt", "r+")
    posicao = arqR.read()
    arqR.close()

    for l in range(linha):
        for c in range(coluna):
            if p == int(posicao):
                colunaDestino = c
                
            p += 1

    return int(colunaDestino)

def defineCorDestino():
    corDestino = "red"
    return corDestino

#DEFINE A IMAGEM DO DESTINO
def defineImagem():
    coringa = Image.open(r'./Images/coringa2.png')  
    basewidth = 60
    wpercent = (basewidth / float(coringa.size[0]))  
    hsize = int((float(coringa.size[1]) * float(wpercent)))
    coringa = coringa.resize((basewidth, hsize), PIL.Image.ANTIALIAS)  
    photo = ImageTk.PhotoImage(coringa)

    return photo