import tkinter as tk  #importa a biblioteca gráfica TKINTER
from pacotes.Mapa import *

#Executa o teste em um mapa de matriz 10x10
mapa = makeMapa("test", 10, 10)

#Preenche os campos do objeto Mapa
for x in range(10):
    for y in range(10):
    	mapa.retangulo[x][y].cor = "blue"

#Atribui o mapa a matriz 10x10
matriz = [[0 for x in range(10)] for y in range(10)]
for x in range(10):
    for y in range(10):
        matriz[x][y] = mapa.retangulo[x][y].cor

#Largura x altura do mapa
largura, altura = 800, 600

#Executor do programa
root = tk.Tk()
root.title("Mapa")
frame = tk.Frame()
frame.pack()

#Utiliza a biblioteca do canvas para desenho da matriz em tela.
canvas = tk.Canvas(frame, width=largura, height=altura)
linhas, colunas = len(matriz), len(matriz[0])

ret_largura, ret_altura = largura // linhas, altura // colunas
for y, linha in enumerate(matriz):
    for x, color in enumerate(linha):
        x0, y0 = x * ret_largura, y * ret_altura
        x1, y1 = x0 + ret_largura-1, y0 + ret_altura-1
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
canvas.pack()

root.mainloop()