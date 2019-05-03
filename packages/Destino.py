from random import randint
import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk

class Destino:
    def __init__(self, linha, coluna):
        self.linha      = defineLinha(linha)
        self.coluna     = defineColuna(coluna)
        self.cor        = defineCorDestino()
        self.imagem     = defineImagem()
        self.posicaoDestino = self.linha * linha + (self.coluna + 1)

def defineLinha(linha):
    linhaDestino = 0
    return linhaDestino

def defineColuna(coluna):
    colunaDestino = 0
    return colunaDestino

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