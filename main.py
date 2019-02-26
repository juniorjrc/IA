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
desenhaMapa(frame, largura, altura, matriz)

root.mainloop()