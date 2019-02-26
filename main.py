from pacotes.Mapa import *

#Define o tamanho da matriz (No caso uma matriz 10 por 10)
m1 = 10
m2 = 10

#Largura x altura do mapa
largura, altura = 800, 600

#Executa o teste em um mapa de matriz 10x10
mapa = makeMapa("test", m1, m2)
matriz = [[0 for x in range(m1)] for y in range(m2)]


populaObjetoMapa(mapa, matriz, m1, m2)

#Executor do programa
root = tk.Tk()
root.title("Mapa")
frame = tk.Frame()
frame.pack()

#Utiliza a biblioteca do canvas para desenho da matriz em tela.
desenhaMapa(largura, altura, matriz)

root.mainloop()